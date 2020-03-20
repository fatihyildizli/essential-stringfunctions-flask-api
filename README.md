# 🤞 essential-string-functions-flask-api
 Flask Python Framework - Essential String Functions API


**String to Binary** 

    curl --location --request POST 'localhost:5000/binary' \
    --form 'input=fatih'

**String Length**

    curl --location --request POST 'localhost:5000/length' \
    --form 'input=fatih'

**String Remove Whitespace**

    curl --location --request POST 'localhost:5000/removewhitespace' \
    --form 'input=fatih'
**String Encoding**

    curl --location --request POST 'localhost:5000/encode' \
        --form 'input=fatih'
**String Decoding**
   
     curl --location --request POST 'localhost:5000/decode' \
            --form 'input=fatih'
**String to Base64**

       curl --location --request POST 'localhost:5000/base64encode' \
                --form 'input=fatih'

**Base64 to String**
 

    curl --location --request POST 'localhost:5000/base64encode' \
                --form 'input=ZmF0aWg='

**String to HEX**

     curl --location --request POST 'localhost:5000/encodehex' \
                    --form 'input=fatih'
