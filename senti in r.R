#install.packages("base64enc")
library(twitteR)
library(base64enc)
library(ROAuth)
library("openssl")
library("httpuv")
library("tm")
library("stringr")
library("dplyr")


packages <- c("twitteR", "openssl")

for(i in packages){
  if(!(i %in% installed.packages()[, "Package"])){
    install.packages(i)
  }
  library(i, character.only = TRUE)
}

setup_twitter_oauth(api_key, api_secret) 

#consumer_key <- "iIzLQajRHS4ymZ0iKrckOYZIx"
#consumer_secret <- "0qmW4MWPCaDpBnSQhhRXVjgJB7sgnPHLzoIKzQEA9uAMg6J6IC"
#access_token <- "1381371098193747974-2SkzmG7LkyI6PHqNx3noCUREe7l01G"
#access_secret <- "KyVYSVRVjVJ4tPz83agLMvSxNGNKLEBqzjjoUkIL2R2nC"

setup_twitter_oauth('iIzLQajRHS4ymZ0iKrckOYZIx', '0qmW4MWPCaDpBnSQhhRXVjgJB7sgnPHLzoIKzQEA9uAMg6J6IC', '1381371098193747974-2SkzmG7LkyI6PHqNx3noCUREe7l01G' , 'KyVYSVRVjVJ4tPz83agLMvSxNGNKLEBqzjjoUkIL2R2nC')
origop <- options("httr_oauth_cache")
options(httr_oauth_cache = TRUE)

searchWitter("headphones","Shoes","Phones","nike")

senti_raw <- searchWitter("headphones","Shoes","Phones","nike")
senti_df <- senti_raw %>% strip_retweets() %>% twLisToDF()

senti_df <- senti_df %>% select(text,favouriteCount,created,truncated,longitude,latitude)

knitr::kable(senti_df[1:3,],format="markdown")


GetSentiment <- function(file){
  fileName <- glue("../input/",file,sep="")
  fileName <- trimws(fileName)
  fileText <- glue(read_file(fileName))
  fileText <- gsub("\\$","",fileText)
  
  tokens <- data_frame(text = fileText) %>% unnest_tokens(word,text)


  sentiment <- tokens %>% 
              inner_join(get_sentiments("phones")) %>%
              count(Sentiment) %>%
              spread(sentiment,n,fill=0) %>%
              mutate(sentiment = positive - negative) %>%
              mutate(file = file) %>%
              mutate(year = as.numeric(str_match(file, "\\d{4}"))) %>%
              mutate(president = str_match(file, "(.*?)_")[2])

 
  return(sentiment)
}