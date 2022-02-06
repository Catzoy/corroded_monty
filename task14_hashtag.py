#https://www.codewars.com/kata/52449b062fb80683ec000024/solutions/python
# #The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.

def generate_hashtag(s):
    if (s == "") or len(s) > 140:
        return False
    a = s.split()
    output = "#"
    for i in a:
        output += i.capitalize()
    return output

print(generate_hashtag("    Hello     World   "))