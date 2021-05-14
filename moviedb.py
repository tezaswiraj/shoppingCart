import requests
import pandas as pd
import pprint
output = 'movies.csv'
api_version = 3
api_key = "ae7ad8198d3ddc555f015754ec3d1d88"
query = "The matrix"
api_base_url = f"https://api.themoviedb.org/{api_version}/"
endpoint_path = f"search/movie"
end_point = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={query}"
print(end_point)
data = requests.get(end_point).json()
#pprint.pprint(data)
#print(data.keys())
#movie_ids = set()
#movie_titles = []
movie_data = []

results = data['results']
for result in results:
	title = result['original_title']
	_id = result['id']
#	print(_id,title)
	if requests.get(end_point).status_code in range(200,299):
		movie_data.append(data)
	#movie_ids.add(_id)
	#movie_titles.append(title)

df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output,index=False)

#print(list(movie_ids))	
#print(movie_titles)
#	print(results[0].keys())
#print(results[0]['id'])



