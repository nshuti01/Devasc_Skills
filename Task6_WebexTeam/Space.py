import requests
import json
### WEBEX API TOKEN
### Access Token 12 hours: https://developer.webex.com/docs/api/getting-started (login required)
current_access_token = "ZDY3Nzk4M2ItMzJkNi00MTY0LTliNzItNDE0MjgzZDg4MTFmODg2Njc1MjctNzUy_P0A1_ffe50b97-2b4a-4965-8373-9822eafeddfd"
### RULES
groups_struc           = {} ### YANG CONTAINER
groups_struc['groups'] = [] ### [group_dict]
group_dict             = {} ### YANG LEAF {"group": {group_name": "G" , "members": member_list} }                             
group_list             = [] ### YANG LIST [group_dict]
member_dict            = {} ### YANG LEAF  {"person_name": "x", "email": "y", "group":"z" }
member_list            = [] ### YANG LIST [member_dict]

###
groups_struc = {
 "groups": [
      { "group": { "group_id": "G1" , "group_name": "devasc_skills_Christin" ,    
                   "members": [   
                     {"person_id": "P-1" , "person_name": "Yvan", "email": "yvan.rooseleer@biasc.be"}   
                   ]
                 }
      }
     
   ]
}

def create_webex_spaces(): # using rest api
    access_token = current_access_token 
    url = 'https://api.ciscospark.com/v1/rooms'
    headers = {'Authorization': 'Bearer {}'.format(access_token),'Content-Type': 'application/json' }
    for rec in groups_struc["groups"]:
        create_group_name = rec["group"]["group_name"]
        payload_space={"title": create_group_name}
        if payload_space["title"] != None:  ### avoid errors if room title is unknown
            res_space = requests.post(url, headers=headers, json=payload_space)
            #print(payload_space)
            #print(res_space.text)
            if res_space.status_code < 300:
                NEW_SPACE_ID = res_space.json()["id"]
                #print(type(NEW_SPACE_ID))
                #print(NEW_SPACE_ID)
                for mbr in rec["group"]["members"]:
                    room_id = NEW_SPACE_ID
                    person_email = mbr["email"] 
                    url2 = 'https://api.ciscospark.com/v1/memberships'
                    payload_member = {'roomId': room_id, 'personEmail': person_email}
                    #print(payload_member)
                    res_member = requests.post(url2, headers=headers, json=payload_member)

#### execute main() when called directly        
if __name__ == "__main__":
    create_webex_spaces()