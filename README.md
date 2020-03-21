# 🤞 essential-string-functions-flask-api
 Flask Python Framework - Essential String Functions API
 
https://essentialfy.herokuapp.com/

**String to Binary** 

    curl --location --request POST 'https://essentialfy.herokuapp.com/binary' \
    --form 'input=fatih'

**String Length**

    curl --location --request POST 'https://essentialfy.herokuapp.com/length' \
    --form 'input=fatih'

**String Remove Whitespace**

    curl --location --request POST 'https://essentialfy.herokuapp.com/removewhitespace' \
    --form 'input=fatih'
**String Encoding**

    curl --location --request POST 'https://essentialfy.herokuapp.com/encode' \
        --form 'input=fatih'
**String Decoding**
   
     curl --location --request POST 'https://essentialfy.herokuapp.com/decode' \
            --form 'input=fatih'
**String to Base64**

       curl --location --request POST 'https://essentialfy.herokuapp.com/base64encode' \
                --form 'input=fatih'

**Base64 to String**
 

    curl --location --request POST 'https://essentialfy.herokuapp.com/base64encode' \
                --form 'input=ZmF0aWg='

**String to HEX**

     curl --location --request POST 'https://essentialfy.herokuapp.com/encodehex' \
                    --form 'input=fatih'
