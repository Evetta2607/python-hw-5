def popularity(text):

     text_lower = text.lower()
     text_split = text_lower.split(' ')
     roster=dict()
     for word in text_split:
       if word in roster:
              roster[word] +=1
       else:
              roster[word] =1

     def second_key(item):
       return item[1]
     def first_key(item):
       return item[0]

     roster.items()
     sorted_by_word = sorted(roster.items(), key=first_key)
     sorted_by_popularity=sorted(sorted_by_word, key=second_key, reverse=True)
     sorted_words=list(map(first_key, sorted_by_popularity))
     return sorted_words
     


       
print(popularity('kiWi juaj apple juaJ Apple Apple'))
print(popularity('kIWi aPPle jUaj kiwi Apple juaj kiwi'))
print(popularity('aab aaa aac aab aac aaa x'))  
       
       

       
              
       
       
 