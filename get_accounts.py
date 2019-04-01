from InstagramAPI import InstagramAPI
import sys
import yaml
import csv
import json

def get_business_or_private(user) :
    business_or_private = ''

    if (user['is_business']) :
      business_or_private += 'Busniness'
    if (user['is_private']) :
      if (len(business_or_private) > 0) :
        business_or_private += ', Private'
      else :
        business_or_private += 'Private'
    
    return business_or_private

def logCSV(filename, userInfo):
    user = userInfo['user']
    if ('pk' in user) :
      with open(filename + '.csv', mode='w') as csv_file:
          fieldnames = ['user_id', 'nickname', 'name', 'known', 'business_or_private', 'verified',
            'gender', 'age', 'followers_count', 'follow_count', 'posts_counter',
            'last_post_timestamp','profile_pic_url', 'last_photo_url', 'city', 'status']
          writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

          writer.writeheader()
          writer.writerow({'user_id': user['pk'], 'nickname': user['username'], 'name': user['full_name'], 'known': '', 'business_or_private': get_business_or_private(user), 'verified': user['is_verified'],
            'gender': '', 'age': '', 'followers_count': user['follower_count'], 'follow_count': user['following_count'], 'posts_counter': user['media_count'], 
            'last_post_timestamp': '','profile_pic_url': user['profile_pic_url'], 'last_photo_url': '', 'city': '', 'status': userInfo['status']})

username = "username"
password = "password"

api = InstagramAPI(username = username, password = password)

if (api.login()):
    api.getSelfUsernameInfo()
    userInfo = api.LastJson
    print("Login succes!")
    logCSV('user', userInfo)
else:
    print("Can't login!")