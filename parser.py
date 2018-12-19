import json
import os
## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
import requests
#from parsed_data.models import ChampionData

django.setup()

#from parsed_data.models import <<modelname>>>


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_data():
	data = {}

	response = requests.get('http://ddragon.leagueoflegends.com/cdn/8.13.1/data/en_US/champion.json')
	data = response.json()

	return data

if __name__ == '__main__':
	data_dict = {}
	data_dict = load_data()
	# print(data_dict.keys())   #결과: dict_keys(['type', 'format', 'version', 'data'])
	#data_dict['data']) type은 dict다

	keys = data_dict['data'].keys()

	# for key in keys:
	# 	print(data_dict['data'][key]['name'])
