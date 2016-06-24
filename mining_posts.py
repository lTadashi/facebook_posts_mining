import urllib.request
import json
import sys

def get_json(url):
	resposta = urllib.request.urlopen(url)
	json_string = resposta.read().decode('utf-8')
	json_obj = json.loads(json_string)
	return json_obj

if '--h' in sys.argv:
	print("\nUSE:\n\tfb_comment_mining facebook_page\n\n");
	sys.exit()

# get page name
page = sys.argv[1]

tags = []
for num in range(2, len(sys.argv)):
	tags.append(sys.argv[num])

url_get_posts = "https://graph.facebook.com/v2.4/{p}/posts?access_token=EAACEdEose0cBAMd1ZCDwZBSFJqld1DLjezY73lUAZC4Kme2yaxJ5vkYQQSAVFkFbEtEmTlRAzN7mfZCeRQebQTQ2I0x3BKDSknAMjzhwCsalOeqStfnhdJ9BbkZAcZAoaUQlWc6nZAYZARHFwgiWlCQOr184uVSp7vxgQ9Sx9uXrwwZDZD&limit=100".format(p = page)
json_obj = get_json(url_get_posts)

# get all posts
print("\nGetting posts...");
posts = []
while 'paging' in json_obj:
	if 'next' in json_obj['paging']:
		for post in json_obj['data']:
			posts.append(post)
		json_obj = get_json(json_obj['paging']['next'])
num_posts = len(posts)		
print("Found " + str(num_posts) + " posts.\n")

print("\nSaving posts...");
mining_file_output = open('posts', 'w')
json.dump(posts, mining_file_output);
mining_file_output.close();