In order to get Some comments what you want,you open JD Website with your browser, you will find a product page.
Then you click F12,click on network in  the buttom and click on next page in your page showing the goods
you will find 'productPageComments.action in the below.
this line, show as below.
the one you get will be a base url for crawling later
and you should remember the callback like  'fetchJSON_comment98vv4563',this one will point to the json file including the comments you need


When you get the comments after following my code
you can generate the wordcloud
it is worth noting you can use different image as the mask


step one;
you should cut the string you got with 'jieba.cut'
strp two:
you can joint there words what you cut before
notice:cut_all=True/False.if you choose True as param,the words in this sentence can be split all in sencods

