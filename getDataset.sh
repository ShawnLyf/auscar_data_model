#!/bin/bash

#for each model in carlist.txt file
IFS=$'\n'
rm -r data
mkdir data
for car in $(cat carlist.txt);do
    export model=$car
    scrapy crawl getimgs -O output.json # crawl the current model
    filename=`echo $car | sed 's/\// /'`
    mkdir data/$filename

    num=1
    grep -oE "https://[^\"]+" output.json > urls.txt
    for url in $(cat urls.txt);do
        curl -o "data/$filename/$num.jpg" $url
        ((num++))
    done
    rm urls.txt
done
rm output.json
