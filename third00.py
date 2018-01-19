# -*- coding: utf-8 -*-
#Chucky_Bot

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile

nadya = LINETCR.LINE()
#nadya.login(qr=True)
nadya.login(token='EorG0TG2TJBKoOdIalP8.6S7B6iV24SxpyyIZPkjUga.IIcvj2D0GhObc+ovT0q1z4iQYL+uUc1bO+ADocFVEaI=)
nadya.loginResult()
print "Nadya-Login Success\n\n=====[Sukses Login]====="

reload(sys)
sys.setdefaultencoding('utf-8')


selfMessage ="""
╔═════════════════════════
║            ☆☞ S E L F ☜☆
╠═════════════════════════
╠➩〘Hi〙
╠➩〘Me〙
╠➩〘Mymid〙
╠➩〘Mid @〙
╠➩〘SearchID: (ID LINE)〙
╠➩〘Checkdate (DD/MM/YY)〙
╠➩〘Kalender〙
╠➩〘Steal contact〙
╠➩〘Pp @〙
╠➩〘Cover @〙
╠➩〘Auto like〙
╠➩〘Scbc Text〙
╠➩〘Cbc Text〙
╠➩〘Gbc Text〙
╠➩〘Getbio @〙
╠➩〘Getinfo @〙
╠➩〘Getname @〙
╠➩〘Getprofile @〙
╠➩〘Getcontact @〙
╠➩〘Getvid @〙
╠➩〘Friendlist〙
╚═════════════════════════
"""

botMessage ="""
╔═════════════════════════
║             ☆☞ B O T ☜☆
╠═════════════════════════
╠➩〘Absen〙
╠➩〘Respon〙
╠➩〘Runtime〙
╠➩〘Mycopy @〙
╠➩〘Mybackup〙
╠➩〘Mybio (Text)〙
╚═════════════════════════
"""

mediaMessage ="""
╔═════════════════════════
║           ☆☞ M E D I A ☜☆
╠═════════════════════════
╠➩〘Gift〙
╠➩〘Gift1 @ s/d Gift10 @〙
╠➩〘Giftbycontact〙
╠➩〘Gif gore〙
╠➩〘Google: (Text)〙
╠➩〘Playstore NamaApp〙
╠➩〘Fancytext: Text〙
╠➩〘/musik Judul-Penyanyi〙
╠➩〘/lirik Judul-Penyanyi〙
╠➩〘/musrik Judul-Penyanyi〙
╠➩〘/ig UrsnameInstagram〙
╠➩〘Checkig UrsnameInstagram〙
╠➩〘/apakah Text (Kerang Ajaib)〙
╠➩〘/kapan Text (Kerang Ajaib)〙
╠➩〘/hari Text (Kerang Ajaib)〙
╠➩〘/berapa Text (Kerang Ajaib)〙
╠➩〘/berapakah Text〙
╠➩〘Youtubelink: Judul Video〙
╠➩〘Youtubevideo: Judul Video〙
╠➩〘Youtubesearch: Judul Video〙
╠➩〘Image NamaGambar〙
╠➩〘Say-id Text〙
╠➩〘Say-en Text〙
╠➩〘Say-jp Text〙
╠➩〘Image NamaGambar〙
╠➩〘Tr-id Text (Translate En Ke ID〙
╠➩〘Tr-en Text (Translate ID Ke En〙
╠➩〘Tr-th Text (Translate ID Ke Th〙
╠➩〘Id@en Text (Translate ID Ke En〙
╠➩〘Id@th Text (Translate ID Ke TH〙
╠➩〘En@id Text (Translate En Ke ID〙
╚═════════════════════════
"""

groupMessage ="""
╔═════════════════════════
║           ☆☞ G R O U P ☜☆
╠═════════════════════════
╠➩〘Welcome〙
╠➩〘Say welcome〙
╠➩〘Invite creator〙
╠➩〘Setview〙
╠➩〘Viewseen〙
╠➩〘Gn: (NamaGroup)〙
╠➩〘Tag all〙
╠➩〘Recover〙
╠➩〘Cancel〙
╠➩〘Cancelall〙
╠➩〘Gcreator〙
╠➩〘Ginfo〙
╠➩〘Gurl〙
╠➩〘List group〙
╠➩〘Pict group: (NamaGroup)〙
╠➩〘Spam: (Text)〙
╠➩〘Add all〙
╠➩〘Kick: (Mid)〙
╠➩〘Invite: (Mid)〙
╠➩〘Invite〙
╠➩〘Memlist〙
╠➩〘Getgroup image〙
╠➩〘Urlgroup Image〙
╚═════════════════════════
"""
tjia="ueacedbe88bf6e2c5cf6188b3a4a26e18"

setMessage ="""
╔═════════════════════════
║              ☆☞ S E T ☜☆
╠═════════════════════════
╠➩〘Sambutan on/off〙
╠➩〘Url on/off〙
╠➩〘Alwaysread on/off〙
╠➩〘Sider on/off〙
╠➩〘Contact on/off〙
╠➩〘Simisimi on/off〙
╚═════════════════════════
"""

creatorMessage ="""
╔═════════════════════════
║         ☆☞ C R E A T O R ☜☆
╠═════════════════════════
╠➩〘Admin add @〙
╠➩〘Admin remove @〙
╠➩〘Crash〙
╠➩〘Kickall〙
╠➩〘Bc: (Text)〙
╠➩〘Join group: (NamaGroup〙
╠➩〘Leave group: (NamaGroup〙
╠➩〘Leave all group〙
╠➩〘Tag on/off〙
╠➩〘Bot restart〙
╠➩〘Turn off〙
╚═════════════════════════
"""

adminMessage ="""
╔═════════════════════════
║            ☆☞ A D M I N ☜☆
╠═════════════════════════
╠➩〘Admin list〙
╠➩〘Allprotect on/off〙
╠➩〘Ban〙
╠➩〘Unban〙
╠➩〘Ban @〙
╠➩〘Unban @〙
╠➩〘Ban list〙
╠➩〘Clear ban〙
╠➩〘Kill〙
╠➩〘Kick @〙
╠➩〘Set member: (Jumblah)〙
╠➩〘Ban group: (NamaGroup〙
╠➩〘Del ban: (NamaGroup〙
╠➩〘List ban〙
╠➩〘Kill ban〙
╠➩〘Glist〙
╠➩〘Glistmid〙
╠➩〘Details group: (Gid)〙
╠➩〘Cancel invite: (Gid)〙
╠➩〘Invitemeto: (Gid)〙
╠➩〘Acc invite〙
╠➩〘Removechat〙
╠➩〘Qr on/off〙
╠➩〘Autokick on/off〙
╠➩〘Ghost on/off〙
╠➩〘Autocancel on/off〙
╠➩〘Invitepro on/off〙
╠➩〘Join on/off〙
╠➩〘Joincancel on/off〙
╠➩〘Respon on/off〙
╠➩〘Responkick on/off〙
╚═════════════════════════
"""

helpMessage ="""
╔═════════════════════════
║              ☆☞ H E L P ☜☆
╠═════════════════════════
╠➩〘Help 1〙
╠➩〘Help 2〙
╠➩〘Help 3〙
╠➩〘Help 4〙
╠➩〘Help 5〙
╠➩〘Help 6〙
╠➩〘Help 7〙
╠➩〘Owner〙
╠➩〘Owner〙
╠➩〘Admin〙
╠➩〘Speed〙
╠➩〘Speed test〙
╠➩〘Status〙
╚═════════════════════════
"""


KAC=[nadya]
mid = ["ueacedbe88bf6e2c5cf6188b3a4a26e18"]
admin=["ueacedbe88bf6e2c5cf6188b3a4a26e18"]

contact = nadya.getProfile()
backup1 = nadya.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

responsename = nadya.getProfile().displayName


wait = {
    "LeaveRoom":True,
    "AutoJoin":False,
    "AutoJoinCancel":True,
    "memberscancel":30,
    "Members":1,
    "AutoCancel":False,
    "AutoKick":True,
    'pap':{},
    'invite':{},
    'steal':{},
    'gift':{},
    'likeOn':{},
    'detectMention':True,
    'kickMention':False,      
    'timeline':True,
    "Timeline":True,
    "comment":"Bot Auto Like ©By :line.me/ti/p/4bvwOIMft8 .",    
    "commentOn":True,
    "commentBlack":{},
    "message":"Thx For Add Me (^_^)\nยินดีที่ได้รู้จะจักครับ ヘ(^_^)ヘ",    
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":False,
    "Contact":False,
    "Sambutan":True,
    "Ghost":False,
    "inviteprotect":False,    
    "alwaysRead":False,    
    "Sider":{},
    "Simi":{},    
    "lang":"JP",
    "BlGroup":{}
}

settings = {
    "simiSimi":{}
    }
    
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request    
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      
    
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False    

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
     
def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True


def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendAudio(self, to_, path):
        M = Message()
        M.text = None
        M.to = to_
        M.contentMetadata = None
        M.contentPreview = None
        M.contentType = 3
        M_id = self._client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def bot(op):
    try:

        if op.type == 0:
            return

        if op.type == 5:
           if wait["autoAdd"] == True:
              nadya.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                nadya.sendText(op.param1,str(wait["message"]))


        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = nadya.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        nadya.sendText(op.param1, "สวัสดี " + "☞ " + nick[0] + " ☜" + "\nยินดีต้อนรับ. . .\nแนะนำตัวด้วยนะ (-__-)   ")
                                    else:
                                        nadya.sendText(op.param1, "สวัสดี " + "☞ " + nick[1] + " ☜" + "\nยินดีต้อนรับ. . .\nแนะนำตัวด้วยนะ (-__-)   ")
                                else:
                                    nadya.sendText(op.param1, "สวัสดี " + "☞ " + Name + " ☜" + "\nคุณไม่ได้สอดแนมใช่มั้ย???\nแนะนำตัวด้วยนะ...   ")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass    	      
	      

        if op.type == 22:
            nadya.leaveRoom(op.param1)

        if op.type == 21:
            nadya.leaveRoom(op.param1)


        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    nadya.acceptGroupInvitation(op.param1)

		    
	    if mid in op.param3:	        
                if wait["AutoJoinCancel"] == True:
		    G = nadya.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        nadya.acceptGroupInvitation(op.param1)
                        nadya.sendText(op.param1,"ขอโทษ " + nadya.getContact(op.param2).displayName + "\nสมาชิกน้อยกว่า 30 คน\nสำหรับข้อมูลโปรดติดต่อเจ้าของของเรา")
                        nadya.leaveGroup(op.param1)                        
		    else:
                        nadya.acceptGroupInvitation(op.param1)
			nadya.sendText(op.param1,"☆พิมพ์ ☞Help☜ สำหรับความช่วยเหลือ☆\n☆โปรดใช้อย่างชาญฉลาด ^_^ ☆")
                        		    
 
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = nadya.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        nadya.rejectGroupInvitation(op.param1)
		    else:
                        nadya.acceptGroupInvitation(op.param1)
			nadya.sendText(op.param1,"☆พิมพ์ ☞Help☜ สำหรับความช่วยเหลือ☆\n☆โปรดใช้อย่างชาญฉลาด ^_^ ☆")
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in Bots:
			pass
		    else:
                        nadya.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			nadya.cancelGroupInvitation(op.param1, [op.param3])
			nadya.sendText(op.param1, "ตรวจพบรายการที่ไม่อนุญาต")
		    else:
			pass
			
        if op.type == 13:
            if op.param2 not in Creator:
             if op.param2 not in admin:
              if op.param2 not in Bots:
                if op.param2 in Creator:
                 if op.param2 in admin:
                  if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    nadya.cancelGroupInvitation(op.param1,[op.param3])
                    nadya.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Creator:
                     if op.param2 not in admin:
                      if op.param2 not in Bots:
                        if op.param2 in Creator:
                         if op.param2 in admin:
                          if op.param2 in Bots:
                            pass

        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Creator:
			 if op.param3 in admin:
			  if op.param3 in Bots:
			      pass
		         if op.param2 in Creator:
		          if op.param2 in admin:
		           if op.param2 in Bots:
		               pass
		           else:
		               nadya.kickoutFromGroup(op.param1,[op.param2])
		               if op.param2 in wait["blacklist"]:
		                   pass
		        else:
			    nadya.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Creator:
			        if op.param2 not in admin:
			            if op.param2 not in Bots:
                                        nadya.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        nadya.inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("ลูกค้า Kick ระเบียบหรือเพราะมันไม่ได้อยู่ในกลุ่ม\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Creator:
			        if op.param2 in admin:
			            if op.param2 in Bots:
			              pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Creator:
		            if op.param2 in admin:
		                if op.param2 in Bots:
			             pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass


                if mid in op.param3:
                    if op.param2 in Creator:
                      if op.param2 in Bots:
                        pass
                    try:
                        nadya.kickoutFromGroup(op.param1,[op.param2])
			nadya.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    nadya.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("ลูกค้า Kick ระเบียบหรือเพราะมันไม่ได้อยู่ในกลุ่ม\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

 
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        nadya.kickoutFromGroup(op.param1,[op.param2])
			nadya.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                nadya.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        nadya.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("ลูกค้า Kick ระเบียบหรือเพราะมันไม่ได้อยู่ในกลุ่ม\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    nadya.inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True


        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Creator:
		 if op.param2 in admin:
		  if op.param2 in Bots:
		   pass		
		else:
                    nadya.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass


        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            ginfo = nadya.getGroup(op.param1)
            contact = nadya.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            nadya.sendText(op.param1,"สวัสดี " + nadya.getContact(op.param2).displayName + "\nยินดีตอนรับ สู่กลุ่ม☞ " + str(ginfo.name) + " ☜" + "\nโปรดอ่านที่โน้ตกลุ่มด้วยนะ\nขอให้มีความสุขกับกลุ่มนี้ ^_^")
            nadya.sendImageWithURL(op.param1,image)
            print "สมาชิกเข้าร่วมกลุ่ม"

        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            nadya.sendText(op.param1,"ลาก่อนนะ " + nadya.getContact(op.param2).displayName +  "\nแล้วเจอกัลใหม่นะ . . .บ๊ายบายย (p′︵‵。) 🤗")
            nadya.inviteIntoGroup(op.param1,[op.param2])
            print "สมาชิกได้ออกจากกลุ่มแล้ว"
            
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                nadya.sendText(msg.to,data['result']['response'].encode('utf-8'))

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = nadya.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Aku Bilang Jangan Ngetag Lagi " + cName + "\nAku Kick Kamu! Sorry, Byee!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  nadya.sendText(msg.to,ret_)
                                  nadya.kickoutFromGroup(msg.to,[msg.from_])
                                  break                              
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = nadya.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag!! Lagi Sibuk",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","-_-","Dia Lagi Off", cName + " Kenapa Tag Saya?","Dia Lagi Tidur\nJangan Di Tag " + cName, "Jangan Suka Tag Gua " + cName, "Kamu Siapa " + cName + "?", "Ada Perlu Apa " + cName + "?","Woii " + cName + " Jangan Ngetag, Riibut!"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  nadya.sendText(msg.to,ret_)
                                  break             


        if op.type == 25:
            msg = op.message


            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    nadya.sendChatChecked(msg.from_,msg.id)
                else:
                    nadya.sendChatChecked(msg.to,msg.id)
                    
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     nadya.like(url[25:58], url[66:], likeType=1005)
                     nadya.comment(url[25:58], url[66:], wait["comment"])
                     nadya.sendText(msg.to,"Like สำเร็จ")                     
                     wait['likeOn'] = False


            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            nadya.sendText(msg.to,"สำเร้จ")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            nadya.sendText(msg.to,"ที่เพิ่ม")
		    else:
			nadya.sendText(msg.to,"ตรวจพบผู้ดูแลแล้ว~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        nadya.sendText(msg.to,"หายไป")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        nadya.sendText(msg.to,"ไม่มีรายชื่อในแบล็คลิส")
            
                    
 
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     nadya.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = nadya.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = nadya.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         nadya.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                     else:
                         contact = nadya.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = nadya.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         nadya.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))


 
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = nadya.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        nadya.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        nadya.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        nadya.sendText(msg.to,"ไม่สามารถใช้นอกกลุ่มได้")
                    else:
                        nadya.sendText(msg.to,"ไม่ใช้งานน้อยกว่ากลุ่ม")
                        

 
            elif msg.text is None:
                return
 
            elif msg.text in ["Creator","Owner"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': tjia}
                nadya.sendMessage(msg)
		nadya.sendText(msg.to,"ผู้ดูแลของเรา (^_^)")
		
            elif msg.text in ["Admin","แอดมิน"]:
                msg.contentType = 13
                admin1 = "ueacedbe88bf6e2c5cf6188b3a4a26e18"
                admin2 = "ueacedbe88bf6e2c5cf6188b3a4a26e18"
                admin3 = "ueacedbe88bf6e2c5cf6188b3a4a26e18"
                msg.contentMetadata = {'mid': tjia}
                nadya.sendMessage(msg)
                msg.contentMetadata = {'mid': admin1}
                nadya.sendMessage(msg)
                msg.contentMetadata = {'mid': admin2}
                nadya.sendMessage(msg)
                msg.contentMetadata = {'mid': admin3}
                nadya.sendMessage(msg)                
		nadya.sendText(msg.to,"นั่นคือ Admin ของเรา (^_^)")	
		
 
                
             elif "Admin add @" in msg.text:
              if msg.from_ in Creator:
                print "[Command]Admin add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = nadya.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   nadya.sendText(msg.to,"Contact Tidak Di Temukan")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            nadya.sendText(msg.to,"Admin Chucky Ditambahkan")
                        except:
                            pass
                print "[Command]Admin add executed"
              else:
                nadya.sendText(msg.to,"Command Denied.")
                nadya.sendText(msg.to,"Creator Permission Required.")
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in Creator:
                print "[Command]Admin Remove Executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = nadya.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   nadya.sendText(msg.to,"Contact Tidak Di Temukan")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            nadya.sendText(msg.to,"Admin Chucky Dihapus")
                        except:
                            pass
                print "[Command]Admin remove executed"
              else:
                nadya.sendText(msg.to,"Command Denied.")
                nadya.sendText(msg.to,"Creator Permission Required.")
                
            elif msg.text in ["Admin list","แอดมินลิส","List admin"]:
              if admin == []:
                  nadya.sendText(msg.to,"รายชื่อผู้ดูแลระบบว่างเปล่า")
              else:
                  nadya.sendText(msg.to,"แปป...")
                  mc = "╔═════════════════════════\n║        ☆☞ ADMIN ☜☆\n╠═════════════════════════\n"
                  for mi_d in admin:
                      mc += "╠••> " +nadya.getContact(mi_d).displayName + "\n"
                  nadya.sendText(msg.to,mc + "╚═════════════════════════")
                  print "[Command]ดำเนินการรายการผู้ดูแลระบบแล้ว"
                 

 

	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = nadya.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                nadya.sendMessage(msg)
		nadya.sendText(msg.to,"เป็นผู้สร้างกลุ่มนี้")
 

                
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    nadya.sendText(msg.to,msg.text)

            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = nadya.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[เป้าหมาย] ถูกขโมย"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                nadya.findAndAddContactsByMid(target)
                                contact = nadya.getContact(target)
                                cu = nadya.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                nadya.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                nadya.sendText(msg.to,"Profile Picture " + contact.displayName)
                                nadya.sendImageWithURL(msg.to,image)
                                nadya.sendText(msg.to,"Cover " + contact.displayName)
                                nadya.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass


            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = nadya.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[เป้าหมาย] ของขวัญ"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                nadya.sendText(msg.to,"ของขวัญถูกส่งแล้ว!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                nadya.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break


            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = nadya.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             nadya.sendText(msg.to, _name + " อยู่ในกลุ่มนี้")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 nadya.findAndAddContactsByMid(target)
                                 nadya.inviteIntoGroup(msg.to,[target])
                                 nadya.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      nadya.sendText(msg.to,"จำกัด การเชิญ")
                                      wait['invite'] = False
                                      break
                                  
 
            elif msg.text in ["Key 1","help 1","Help 1"]:
                nadya.sendText(msg.to,creatorMessage)

            elif msg.text in ["Key 2","help 2","Help 2"]:
                nadya.sendText(msg.to,groupMessage)

            elif msg.text in ["Key","help","Help"]:
                nadya.sendText(msg.to,helpMessage)

            elif msg.text in ["Key 3","help 3","Help 3"]:
                nadya.sendText(msg.to,selfMessage)

            elif msg.text in ["Key 4","help 4","Help 4"]:
                nadya.sendText(msg.to,botMessage)

            elif msg.text in ["Key 5","help 5","Help 5"]:
                nadya.sendText(msg.to,setMessage)

            elif msg.text in ["Key 6","help 6","Help 6"]:
                nadya.sendText(msg.to,mediaMessage)
                
            elif msg.text in ["Key 7","help 7","Help 7"]:
                nadya.sendText(msg.to,adminMessage)                
                

 
            elif msg.text in ["List group"]:
                    gid = nadya.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = nadya.getGroup(i).name
                        h += "♦【%s】\n" % (gn)
		        jml += 1
                    nadya.sendText(msg.to,"=======[List Group]=======\n"+ h +"\nTotal Group: "+str(jml))
 
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = nadya.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
		        h = nadya.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    nadya.sendText(msg.to, "สำเร้จ Ban Group : "+grp)
			else:
			    pass
		else:
		    nadya.sendText(msg.to, "OK")
 
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        nadya.sendText(msg.to,"ยังไม่มีข้อความ")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +nadya.getGroup(gid).name + "\n"
                        nadya.sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    nadya.sendText(msg.to, "OK")
 
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if nadya.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    nadya.sendText(msg.to, "ลบแบนสำเร้จ "+ng)
		        else:
			    pass
		else:
		    nadya.sendText(msg.to, "Ok")
 
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = nadya.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = nadya.getGroup(i).name
		            if h == ng:
		                nadya.inviteIntoGroup(i,[Creator])
			        nadya.sendText(msg.to,"เข้าร่วมสำเร้จ ["+ h +"] Group")
			    else:
			        pass
		    else:
		        nadya.sendText(msg.to,"OK")
		except Exception as e:
		    nadya.sendText(msg.to, str(e))
 
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = nadya.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = nadya.getGroup(i).name
		        if h == ng:
			    nadya.sendText(i,"Bot บังคับให้ออกโดยเจ้าของ!")
		            nadya.leaveGroup(i)
			    nadya.sendText(msg.to,"Success Left ["+ h +"] group")
			else:
			    pass
		else:
		    nadya.sendText(msg.to,"Ok")
 
	    elif "Leave all group" == msg.text:
		gid = nadya.getGroupIdsJoined()
                if msg.from_ in Creator:
		    for i in gid:
			nadya.sendText(i,"Bot บังคับให้ออกโดยเจ้าของ!")
		        nadya.leaveGroup(i)
		    nadya.sendText(msg.to,"ความสำเร็จออกจากกลุ่มทั้งหมด")
		else:
		    nadya.sendText(msg.to,"OK")
		   

            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = nadya.getGroupIdsJoined()
                for i in gid:
                    h = nadya.getGroup(i).name
                    gna = nadya.getGroup(i)
                    if h == saya:
                        nadya.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		    
		    
 
            elif msg.text in ["cancelall","Cancelall"]:
                if msg.toType == 2:
                    X = nadya.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        nadya.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        nadya.sendText(msg.to,"ไม่รอดำเนินการ")
                else:
                    nadya.sendText(msg.to,"ไม่สามารถใช้นอกกลุ่ม")
 
            elif msg.text in ["Ourl","Url on"]:
                if msg.toType == 2:
                    X = nadya.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    nadya.updateGroup(X)
                    nadya.sendText(msg.to,"Url อยู่แล้ว")
                else:
                    nadya.sendText(msg.to,"ไม่สามารถใช้นอกกลุ่มได้")
 
            elif msg.text in ["Curl","Url off"]:
                if msg.toType == 2:
                    X = nadya.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    nadya.updateGroup(X)
                    nadya.sendText(msg.to,"URL ปิดอยู่")

                else:
                    nadya.sendText(msg.to,"ไม่สามารถใช้นอกกลุ่มได้")
 
            elif msg.text in ["Join on","Autojoin on"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    wait["AutoJoinCancel"] = False
                    nadya.sendText(msg.to,"เข้าร่วมอัตโนมัติแล้ว")
		else:
		    nadya.sendText(msg.to,"ok")

            elif msg.text in ["Join off","Autojoin off"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = False
                    nadya.sendText(msg.to,"เข้าร่วมอัตโนมัติปิดใช้งานแล้ว")
		else:
		    nadya.sendText(msg.to,"OK")
		    
		    
            elif msg.text in ["Joincancel on","Autojoincancel on"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = True
                    wait["AutoJoin"] = False
                    nadya.sendText(msg.to,"ยกเลิกการเข้าร่วมอัตโนมัติเปิดอยู่")
		else:
		    nadya.sendText(msg.to,"OK")

            elif msg.text in ["Joincancel off","Autojoincancel off"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = False
                    nadya.sendText(msg.to,"เข้าร่วมอัตโนมัติยกเลิกถูกปิดใช้งานแล้ว")
		else:
		    nadya.sendText(msg.to,"OK")		    
		    
 
            elif msg.text in ["Respon on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["kickMention"] = False
                    nadya.sendText(msg.to,"การตอบกลับอัตโนมัติเปิดอยู่")
		else:
		    nadya.sendText(msg.to,"OK")

            elif msg.text in ["Respon off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    nadya.sendText(msg.to,"การตอบกลับอัตโนมัติปิดอยู่")
		else:
		    nadya.sendText(msg.to,"OK")	
		    
		    
 
            elif msg.text in ["Responkick on"]:
		if msg.from_ in admin:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    nadya.sendText(msg.to,"เปิดใช้งาน Kick Auto Response แล้ว")
		else:
		    nadya.sendText(msg.to,"OK")

            elif msg.text in ["Responkick off"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False                    
                    nadya.sendText(msg.to,"ปิดใช้งาน Kick Auto Response แล้ว")
		else:
		    nadya.sendText(msg.to,"OK")			  
		    
 
	    elif msg.text in ["Autocancel on"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = True
                nadya.sendText(msg.to,"ยกเลิกอัตโนมัติเปิดอยู่")
		print wait["AutoCancel"]
	     else:
		    nadya.sendText(msg.to,"OK")		

	    elif msg.text in ["Autocancel off"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = False
                nadya.sendText(msg.to,"ยกเลิกอัตโนมัติแล้ว")
		print wait["AutoCancel"]
	     else:
		    nadya.sendText(msg.to,"OK")	
		    

	    elif msg.text in ["Invitepro on"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = True
                nadya.sendText(msg.to,"เชิญป้องกันอยู่ใน")
		print wait["inviteprotect"]
	     else:
		    nadya.sendText(msg.to,"OK")		

	    elif msg.text in ["Invitepro off"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = False
                nadya.sendText(msg.to,"การเชิญป้องกันปิดอยู่")
		print wait["inviteprotect"]
	     else:
		    nadya.sendText(msg.to,"OK")		    

	    elif "Qr on" in msg.text:
	     if msg.from_ in admin:	        
	        wait["Qr"] = True
	    	nadya.sendText(msg.to,"QR Protect เปิดอยู่")
	     else:
		    nadya.sendText(msg.to,"OK")	    	

	    elif "Qr off" in msg.text:
	     if msg.from_ in admin:	        
	    	wait["Qr"] = False
	    	nadya.sendText(msg.to,"Qr Protect ปิดอยู่")
	     else:
		    nadya.sendText(msg.to,"OK")	    	

                        

	    elif "Autokick on" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = True
		     nadya.sendText(msg.to,"Auto Kick เปิดอยู่")
	     else:
	        nadya.sendText(msg.to,"OK")	     

	    elif "Autokick off" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = False
		     nadya.sendText(msg.to,"Auto Kick ปิดอยู่")
	     else:
	        nadya.sendText(msg.to,"OK")	     

	    elif "Ghost on" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["Ghost"] = True
		     nadya.sendText(msg.to,"Ghost เปิดอยู่")
	     else:
	        nadya.sendText(msg.to,"OK")		     

	    elif "Ghost off" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["Ghost"] = False
		     nadya.sendText(msg.to,"Ghost ถูกปิดใช้แล้ว")
	     else:
	         nadya.sendText(msg.to,"OK")		     

            elif msg.text in ["Allprotect on"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = True
                    wait["inviteprotect"] = True                   
                    wait["AutoKick"] = True
                    wait["Qr"] = True
                    wait["Ghost"] = True                     
                    nadya.sendText(msg.to,"การป้องกันทั้งหมดเปิดอยู่ทั้งหมด")
		else:
		    nadya.sendText(msg.to,"OK")

            elif msg.text in ["Allprotect off"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = False
                    wait["inviteprotect"] = False                    
                    wait["AutoKick"] = False
                    wait["Qr"] = False
                    wait["Ghost"] = False                    
                    nadya.sendText(msg.to,"ป้องกันทั้งหมดถูกปิดใช้งานทั้งหมด")
		else:
		    nadya.sendText(msg.to,"OK")


            elif msg.text in ["K on","Contact on"]:
                wait["Contact"] = True
                nadya.sendText(msg.to,"เปิดการติดต่อแล้ว")

            elif msg.text in ["K off","Contact off"]:
                wait["Contact"] = False
                nadya.sendText(msg.to,"ปิดการติดต่อแล้ว")
                

            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                nadya.sendText(msg.to,"Always Read เปิดอยู่")

            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                nadya.sendText(msg.to,"อ่านแล้วเสมอ")                


            elif msg.text in ["Sambutan on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        nadya.sendText(msg.to,"เปิดใช้งานคำอวยพรแล้วヾ(*´∀｀*)ﾉ")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        nadya.sendText(msg.to,"เปิดแล้วヽ(´▽｀)/")

            elif msg.text in ["Sambutan off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        nadya.sendText(msg.to,"ปิดการใช้งานคำอวยพรแล้ว(　＾∇＾)")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        nadya.sendText(msg.to,"ปิดแล้ว(p′︵‵。)")
                        
                        
            elif "Sider on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                nadya.sendText(msg.to,"พร้อมในการตรวจสอบ Sider")
                
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    nadya.sendText(msg.to, "Cek Sider ปิด")
                else:
                    nadya.sendText(msg.to, "OK")                         


            elif msg.text in ["Status"]:
                md = ""
		if wait["Sambutan"] == True: md+="╠➩✔️ Sambutan : On\n"
		else:md+="╠➩❌ Sambutan : Off\n"
		if wait["AutoJoin"] == True: md+="╠➩✔️ Auto Join : On\n"
                else: md +="╠➩❌ Auto Join : Off\n"
		if wait["AutoJoinCancel"] == True: md+="╠➩✔️ Auto Join Cancel : On\n"
                else: md +="╠➩❌ Auto Join Cancel : Off\n"                
		if wait["Contact"] == True: md+="╠➩✔️ Info Contact : On\n"
		else: md+="╠➩❌ Info Contact : Off\n"
                if wait["AutoCancel"] == True:md+="╠➩✔️ Auto Cancel : On\n"
                else: md+= "╠➩❌ Auto Cancel : Off\n"
                if wait["inviteprotect"] == True:md+="╠➩✔️ Invite Protect : On\n"
                else: md+= "╠➩❌ Invite Protect : Off\n"                
		if wait["Qr"] == True: md+="╠➩✔️ Qr Protect : On\n"
		else:md+="╠➩❌ Qr Protect : Off\n"
		if wait["AutoKick"] == True: md+="╠➩✔️ Auto Kick : On\n"
		else:md+="╠➩❌ Auto Kick : Off\n"
		if wait["Ghost"] == True: md+="╠➩✔️ Ghost : On\n"
		else:md+="╠➩❌ Ghost : Off\n"
		if wait["alwaysRead"] == True: md+="╠➩✔️ Always Read : On\n"
		else:md+="╠➩❌ Always Read: Off\n"
		if wait["detectMention"] == True: md+="╠➩✔️ Auto Respon : On\n"
		else:md+="╠➩❌ Auto Respon : Off\n"		
		if wait["kickMention"] == True: md+="╠➩✔️ Auto Respon Kick : On\n"
		else:md+="╠➩❌ Auto Respon Kick : Off\n"				
		if wait["Sider"] == True: md+="╠➩✔️ Auto Sider : On\n"
		else:md+="╠➩❌ Auto Sider: Off\n"	
		if wait["Simi"] == True: md+="╠➩✔️ Simisimi : On\n"
		else:md+="╠➩❌ Simisimi: Off\n"		
                nadya.sendText(msg.to,"╔═════════════════════════\n""║           ☆☞ S T A T U S ☜☆\n""╠═════════════════════════\n"+md+"╚═════════════════════════")


            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                nadya.sendMessage(msg)
                
                
            elif "Gift1 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"ไม่มีผู้ใช้")
                           pass
                       else:
                           for target in targets:
                                try:
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"ไม่มีผู้ใช้")
                           pass
                       else:
                           for target in targets:
                                try:
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"ไม่มีผู้ใช้")
                           pass
                       else:
                           for target in targets:
                                try:
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"ไม่มีผู้ใช้")
                           pass
                       else:
                           for target in targets:
                                try:
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1329191'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift5 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"ไม่มีผู้ใช้")
                           pass
                       else:
                           for target in targets:
                                try:
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '9057'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift6 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"ไม่มีผู้ใช้")
                           pass
                       else:
                           for target in targets:
                                try:
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '9167'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift7 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"ไม่มีผู้ใช้")
                           pass
                       else:
                           for target in targets:
                                try:
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '7334'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift8 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"ไม่มีผู้ใช้")
                           pass
                       else:
                           for target in targets:
                                try:
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift9 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift9 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"ไม่มีผู้ใช้")
                           pass
                       else:
                           for target in targets:
                                try:
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1405277'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift10 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"ไม่มีผู้ใช้")
                           pass
                       else:
                           for target in targets:
                                try:
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}


            elif msg.text.lower() in ["wkwkwk","wkwk","hahaha","haha"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '100',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["hehehe","ฮิฮิ"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '10',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["galau"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '9',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["you","คุณ","คุน"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '7',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["marah","hadeuh","hadeh"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '6',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["please","pliss","mohon","ได้โปรด"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '4',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["haa","haaa","ฮาฮาฮา","555"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '3',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["lucu","ngakak","lol"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '110',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["hmm","hmmm"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '101',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["tidur"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '1',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["gemes"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '2',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["cantik","imut"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '5',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["nyanyi","lalala"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '11',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["gugup"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '8',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["ok","oke","okay","oce","okee","sip","siph"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '13',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["mantab","mantap","nice","keren"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '14',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["ngejek"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '15',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["nangis","sedih"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '16',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["woi","kampret"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '102',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["huft"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '104',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)
                
        


            elif msg.text in ["Tagall","Tag all"]:
                  group = nadya.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      nadya.sendMessage(msg)
                  except Exception as error:
                      print error


            elif msg.text in ["Setview","Setpoint","Cctv"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                nadya.sendText(msg.to, "☆Checkpoint Checked☆")
                print "Setview"

            elif msg.text in ["Viewseen","Check","Ciduk","Cyduk"]:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = nadya.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "╔═════════════════════════\n║         ☆☞ LIST VIEWERS ☜☆\n╠═════════════════════════\n╠➩"
                        grp = '\n╠➩ '.join(str(f) for f in dataResult)
                        total = '\n╠═════════════════════════\n╠➩ Total %i Viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n╚═════════════════════════"
                        nadya.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                        nadya.sendText(msg.to, "☆Auto Checkpoint☆")                        
                    else:
                        nadya.sendText(msg.to, "☆ไม่มีผู้ชม☆")
                    print "Viewseen"


	    elif "Kick " in msg.text:
		if msg.from_ in admin:	        
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    nadya.kickoutFromGroup(msg.to,[mention['M']])

	    elif "Set member: " in msg.text:
		if msg.from_ in admin:	 	        
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    nadya.sendText(msg.to, "มีการตั้งค่าจำนวนสมาชิกขั้นต่ำแล้ว : "+jml)

	    elif "Add all" in msg.text:
		    thisgroup = nadya.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    nadya.findAndAddContactsByMids(mi_d)
		    nadya.sendText(msg.to,"สำเร้จ Add all")


            elif msg.text in ["Invite"]:
                wait["invite"] = True
                nadya.sendText(msg.to,"ส่ง Contact")
                
                

            elif msg.text in ["Auto like"]:
                wait["likeOn"] = True
                nadya.sendText(msg.to,"Shere โพสต์ที่คุณต้องการ!")                


            elif msg.text in ["Steal contact"]:
                wait["steal"] = True
                nadya.sendText(msg.to,"ส่ง Contact")
                

            elif msg.text in ["Giftbycontact"]:
                wait["gift"] = True
                nadya.sendText(msg.to,"ส่ง Contact") 
                

	    elif "Recover" in msg.text:
		thisgroup = nadya.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		nadya.createGroup("Recover", mi_d)
		nadya.sendText(msg.to,"สำเร้จ recover")



            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = nadya.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    nadya.updateGroup(X)
                else:
                    nadya.sendText(msg.to,"ไม่สามารถใช้นอกเหนือจากกลุ่มได้.")

            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		if midd not in admin:
		    nadya.kickoutFromGroup(msg.to,[midd])
		else:
		    nadya.sendText(msg.to,"ตรวจพบผู้ดูแลแล้ว")

            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                nadya.findAndAddContactsByMid(midd)
                nadya.inviteIntoGroup(msg.to,[midd])

            elif "Invite creator" in msg.text:
                midd = "ueacedbe88bf6e2c5cf6188b3a4a26e18"
                nadya.inviteIntoGroup(msg.to,[midd])

            elif msg.text in ["Welcome","welcome","ยินดีต้อนรับ","welkam","Wc","wc"]:
                gs = nadya.getGroup(msg.to)
                nadya.sendText(msg.to,"ยินดีต้อนรับสู่ "+ gs.name)
                msg.contentType = 7
                msg.contentMetadata={'STKID': '247',
                                    'STKPKGID': '3',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = nadya.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
			nadya.sendText(i,"=======[BROADCAST]=======\n\n"+bc+"\n\nContact Me : line.me/ti/p/4bvwOIMft8")
		    nadya.sendText(msg.to,"Success BC BosQ")
		else:
		    nadya.sendText(msg.to,"OK Admin")

            elif msg.text in ["Cancel"]:
                gid = nadya.getGroupIdsInvited()
                for i in gid:
                    nadya.rejectGroupInvitation(i)
                nadya.sendText(msg.to,"คำเชิญทั้งหมดถูกปฏิเสธ")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = nadya.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        nadya.updateGroup(x)
                    gurl = nadya.reissueGroupTicket(msg.to)
                    nadya.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        nadya.sendText(msg.to,"ไม่สามารถใช้นอกกลุ่มได้")
                    else:
                        nadya.sendText(msg.to,"ไม่ใช้งานน้อยกว่ากลุ่ม")


            elif msg.text in ["timeline"]:
		try:
                    url = nadya.activity(limit=5)
		    nadya.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E

            elif msg.text in ["@bye","@Bye"]:
		    nadya.leaveGroup(msg.to)		    
		    

            elif msg.text in ["Absen"]:
		nadya.sendText(msg.to,"Hadir!!")


            elif msg.text.lower() in ["respon"]:
                nadya.sendText(msg.to,responsename)

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                print("Speed")                
                elapsed_time = time.time() - start
		nadya.sendText(msg.to, "Progress...")
                nadya.sendText(msg.to, "%sseconds" % (elapsed_time))
                
            elif msg.text in ["Speed test"]:
                start = time.time()
                nadya.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                nadya.sendText(msg.to, "%sseconds" % (elapsed_time))                
 
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    nadya.sendText(msg.to,"send contact")

            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    nadya.sendText(msg.to,"send contact")
 
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                  if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = nadya.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        nadya.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    nadya.sendText(msg.to,"Succes BosQ")
                                except:
                                    nadya.sendText(msg.to,"Error")
			    else:
				nadya.sendText(msg.to,"ตรวจพบผู้ดูแลแล้ว~")
 
            elif msg.text in ["Banlist","Ban list"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    nadya.sendText(msg.to,"ยังไม่มีข้อความ")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +nadya.getContact(mi_d).displayName + "\n"
                    nadya.sendText(msg.to,"===[Blacklist User]===\n"+mc)

 
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                if msg.from_ in admin:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = nadya.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        nadya.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                nadya.sendText(msg.to,"Succes BosQ")
                            except:
                                nadya.sendText(msg.to,"Succes BosQ")
                                
                                
            elif msg.text.lower() == 'clear ban':
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    nadya.sendText(msg.to,"ヽ( ^ω^)ﾉ└ ❉ยกเลิกแบนทั้งหมดสำเร้จ❉ ┐") 

            elif msg.text.lower() in ["bot","third"]:
                nadya.sendText(msg.to,"โทรหาฉัน ~ โทรหาฉัน!?") 
                nadya.sendText(msg.to,"☆พิมพ์ ☞Help☜ สำหรับความช่วยเหลือ☆") 

 
            elif msg.text in ["Kill ban"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = nadya.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            nadya.sendText(msg.to,"ไม่มีผู้ใช้บัญชีดำ")
                            return
                        for jj in matched_list:
                            nadya.kickoutFromGroup(msg.to,[jj])
                        nadya.sendText(msg.to,"บัญชีดำจำเป็นต้องถูกลบออกจริงๆ")
		else:
		    nadya.sendText(msg.to, "ผู้สร้างพิเศษ")
 
            elif msg.text in ["Kill"]:
                    if msg.toType == 2:
                      if msg.from_ in admin:
                        group = nadya.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            nadya.sendText(msg.to,"Fuck You")
                            return
                        for jj in matched_list:
                            try:
                                nadya.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass

 
            elif "Kickall" == msg.text:
		    if msg.from_ in Creator:
                     if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("Kickall","")
                        gs = nadya.getGroup(msg.to)
                        nadya.sendText(msg.to,"เรียบร้อย~")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            nadya.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
				if target not in admin:
                                    try:
                                        nadya.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        nadya.sendText(msg.to,str(e))
			    nadya.inviteIntoGroup(msg.to, targets)
 

	    elif msg.text in ["Bot restart","Reboot"]:
		if msg.from_ in Creator:
		    nadya.sendText(msg.to, "Bot ถูกรีสตาร์ทแล้ว...")
		    restart_program()
		    print "@Restart"
		else:
		    nadya.sendText(msg.to, "ไม่มีสิทธิ์เข้าถึง")
		    
            elif msg.text in ["Turn off"]: 
	        if msg.from_ in Creator:                
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass 		    


            elif 'Crash' in msg.text:
              if msg.from_ in Creator:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "THIRD,'"}
                nadya.sendMessage(msg)

 
            elif "Mycopy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Mycopy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = nadya.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       nadya.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               nadya.CloneContactProfile(target)
                               nadya.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e

            elif msg.text in ["Mybackup"]:
                try:
                    nadya.updateDisplayPicture(backup1.pictureStatus)
                    nadya.updateProfile(backup1)
                    nadya.sendText(msg.to, "Done (^_^)")
                except Exception as e:
                    nadya.sendText(msg.to, str(e))

 
	    elif "/musik " in msg.text:
					songname = msg.text.replace("/musik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						nadya.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						nadya.sendText(msg.to, "Lagu " + song[0] + "\nใน Prosses ... รอสักครู่ ^_^ ")
						nadya.sendAudioWithURL(msg.to,abc)
						nadya.sendText(msg.to, "ยินดีต้อนรับสู่เพลง " + song[0])
	
            elif '/lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        nadya.sendText(msg.to, hasil)
                except Exception as wak:
                        nadya.sendText(msg.to, str(wak))
                        
	    elif "/musrik " in msg.text:
					songname = msg.text.replace("/musrik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						hasil = 'Lyric Lagu ('
						hasil += song[0]
						hasil += ')\n\n'
						hasil += song[5]
						nadya.sendText(msg.to, "Lagu " + song[0] + "\nใน Prosses ... รอสักครู่ ^_^ ")
						nadya.sendAudioWithURL(msg.to,abc)
						nadya.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4] +"\n\n" + hasil)
						nadya.sendText(msg.to, "ยินดีต้อนรับสู่เพลง " + song[0])
             
            
            
            elif "Fancytext: " in msg.text:
                    txt = msg.text.replace("Fancytext: ", "")
                    nadya.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"


            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = nadya.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        nadya.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = nadya.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                nadya.sendText(msg.to,"Upload image failed.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = nadya.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        nadya.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = nadya.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                nadya.sendText(msg.to,"Upload image failed.")
                                
                                
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = nadya.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        nadya.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = nadya.getContact(target)
                                nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                nadya.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = nadya.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        nadya.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = nadya.getContact(target)
                                nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                nadya.sendText(msg.to,"Upload image failed.")

            elif msg.text.lower() in ["Owner","pap creator"]:
                                link = ["http://dl.profile.line-cdn.net/0hNPsZWL9WEX9OIz0lhyFuKHJmHxI5DRc3NkJaETwkRklqGwQoJkNbTGklHRo2G1B7cxFXH2NxSU03"]
                                pilih = random.choice(link)
                                nadya.sendImageWithURL(msg.to,pilih)

 
            elif "Spam: " in msg.text:
                  bctxt = msg.text.replace("Spam: ", "")
                  t = 10
                  while(t):
                    nadya.sendText(msg.to, (bctxt))
                    t-=1

            elif "Tcbc " in msg.text:
                  bctxt = msg.text.replace("Tcbc ", "")
                  orang = nadya.getAllContactIds()
                  t = 20
                  for manusia in orang:
                    while(t):
                      nadya.sendText(manusia, (bctxt))
                      t-=1

            elif "Tbc " in msg.text:
                  broadcasttxt = msg.text.replace("Tbc ", "") 
                  orang = nadya.getAllContactIds()
                  for manusia in orang:
                    nadya.sendText(manusia, (broadcasttxt))

 
            elif '/ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("/ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html.parser')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO ========\n"
                    details = "\n========INSTAGRAM INFO ========"
                    nadya.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    nadya.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	nadya.sendText(msg.to, str(njer))
                	
                	
            elif "Checkig " in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                nadya.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                nadya.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)                	


            elif 'Youtubelink: ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    nadya.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    nadya.sendText(msg.to,"Could not find it")
                    
                    
            elif 'Youtubevideo: ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubevideo: ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        nadya.sendVideoWithURL(msg.to,'https://www.youtube.com' + results['href'])
                    except:
                        nadya.sendText(msg.to, "Could not find it")                    

 
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")

            elif "Say welcome" in msg.text:
                gs = nadya.getGroup(msg.to)
                say = msg.text.replace("Say welcome","ยินดีต้อนรับสู่ "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")


            elif msg.text.lower() in ["hi","hai","halo","hallo"]:
                    beb = "สวัสดีครับ 😘 " +nadya.getContact(msg.from_).displayName + " 􀸂􀆇หัวใจที่เต็มไปด้วยดวงดาว􏿿"
                    nadya.sendText(msg.to,beb)



            elif "playstore " in msg.text.lower():
                tob = msg.text.lower().replace("playstore ","")
                nadya.sendText(msg.to,"ค้นหาตอนนี้...")
                nadya.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                nadya.sendText(msg.to,"ลิงก์ของเขาไม่ใช่ (^_^)")


            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = nadya.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        nadya.sendText(msg.to, g.mid)
                    else:
                        pass


            elif "Mybio " in msg.text:
                    string = msg.text.replace("Mybio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = nadya.getProfile()
                        profile.statusMessage = string
                        nadya.updateProfile(profile)
                        nadya.sendText(msg.to,"Done")

            elif "Myname " in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("Myname ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = nadya.getProfile()
                        profile.displayName = string
                        nadya.updateProfile(profile)
                        nadya.sendText(msg.to,"Done")



            elif msg.text.lower() in ["mymid","myid"]:
                middd = "Name : " +nadya.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                nadya.sendText(msg.to,middd)

            elif msg.text.lower() in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                nadya.sendMessage(msg)

            elif "/apakah " in msg.text:
                apk = msg.text.replace("/apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")
                
            elif "/hari " in msg.text:
                apk = msg.text.replace("/hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")                


            elif "/berapa " in msg.text:
                apk = msg.text.replace("/berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")
                
            elif "/berapakah " in msg.text:
                apk = msg.text.replace("/berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")                

            elif "/kapan " in msg.text:
                apk = msg.text.replace("/kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")

 
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                nadya.sendText(msg.to," Simsimi เปิดการใช้งาน")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                nadya.sendText(msg.to,"Simsimi ปิดการใช้งาน")

 
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    nadya.sendImageWithURL(msg.to,path)
                except:
                    pass
 
            elif "Youtubesearch: " in msg.text:
                    query = msg.text.replace("Youtube ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        nadya.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'


 
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                nadya.sendText(msg.to, A)

            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                nadya.sendText(msg.to, A)
                
            elif "Tr-th " in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                nadya.sendText(msg.to, A)                

            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                nadya.sendText(msg.to,"----อินโดนีเซีย----\n" + "" + kata + "\n\n----อังกฤษ----\n" + "" + result)


            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                nadya.sendText(msg.to,"----อังกฤษ----\n" + "" + kata + "\n\n----อินโดนีเซีย----\n" + "" + result)
                
            
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                nadya.sendText(msg.to,"----อินโดนีเซีย----\n" + "" + kata + "\n\n----ไทยแลนด์----\n" + "" + result)
                
            
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                nadya.sendText(msg.to,"----ไทยแลนด์----\n" + "" + kata + "\n\n----อินโดนีเซีย----\n" + "" + result)                
 
            elif msg.text in ["Friendlist"]:    
                contactlist = nadya.getAllContactIds()
                kontak = nadya.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                nadya.sendText(msg.to, msgs)

            elif msg.text in ["Memlist"]:   
                kontak = nadya.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═�����═══════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                nadya.sendText(msg.to, msgs)

            

 
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = nadya.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    nadya.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = nadya.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            nadya.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"


            elif "Getgroup image" in msg.text:
                group = nadya.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                nadya.sendImageWithURL(msg.to,path)

            elif "Urlgroup image" in msg.text:
                group = nadya.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                nadya.sendText(msg.to,path)
 
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = nadya.getContact(key1)
                cu = nadya.channel.getCover(key1)
                try:
                    nadya.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    nadya.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)


            elif "Getprofile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = nadya.getContact(key1)
                cu = nadya.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    nadya.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    nadya.sendText(msg.to,"Profile Picture " + contact.displayName)
                    nadya.sendImageWithURL(msg.to,image)
                    nadya.sendText(msg.to,"Cover " + contact.displayName)
                    nadya.sendImageWithURL(msg.to,path)
                except:
                    pass


            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = nadya.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                nadya.sendMessage(msg)

            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = nadya.getContact(key1)
                cu = nadya.channel.getCover(key1)
                try:
                    nadya.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    nadya.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))


            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = nadya.getContact(key1)
                cu = nadya.channel.getCover(key1)
                try:
                    nadya.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    nadya.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)


            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot เดินมาแล้วระหว่าง :\n"+waktu(eltime)
                nadya.sendText(msg.to,van)
                
                 
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                nadya.sendText(msg.to,"========== I N F O R M A S I ==========\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n========== I N F O R M A S I ==========")
                
   
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                bulan = ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                nadya.sendText(msg.to, rst)                
                 
                
            elif "SearchID: " in msg.text:
                userid = msg.text.replace("SearchID: ","")
                contact = nadya.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                nadya.sendMessage(msg)
                
            elif "Searchid: " in msg.text:
                userid = msg.text.replace("Searchid: ","")
                contact = nadya.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                nadya.sendMessage(msg)       
                
                
            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        nadya.removeAllMessages(op.param2)
                        print "[Command] ลบแชท"
                        nadya.sendText(msg.to,"เรียบร้อย")
                    except Exception as error:
                        print error
                        nadya.sendText(msg.to,"Error")      
                        
                        
            elif "Invitemeto: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Invitemeto: ","")
                    if gid == "":
                        nadya.sendText(msg.to,"รหัสกลุ่มไม่ถูกต้อง")
                    else:
                        try:
                            nadya.findAndAddContactsByMid(msg.from_)
                            nadya.inviteIntoGroup(gid,[msg.from_])
                        except:
                            nadya.sendText(msg.to,"บางทีฉันอาจไม่อยู่ในกลุ่ม")


            elif msg.text in ["Glist"]:
                nadya.sendText(msg.to, "รอสักครู่. . .")                    
                gid = nadya.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠➩" + "%s\n" % (nadya.getGroup(i).name +" ~> ["+str(len(nadya.getGroup(i).members))+"]")
                nadya.sendText(msg.to,"╔═════════════════════════\n║          ☆☞ LIST GROUPS☜☆\n╠═════════════════════════\n" + h + "╠═════════════════════════" + "\n║ Total Groups =" +" ["+str(len(gid))+"]\n╚═════════════════════════")

            elif msg.text in ["Glistmid"]:   
                gruplist = nadya.getGroupIdsJoined()
                kontak = nadya.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                nadya.sendText(msg.to, msgs)



            elif "Google: " in msg.text:
                    a = msg.text.replace("Google: ","")
                    b = urllib.quote(a)
                    nadya.sendText(msg.to,"Sedang Mencari...")
                    nadya.sendText(msg.to, "https://www.google.com/" + b)
                    nadya.sendText(msg.to,"Itu Dia Linknya. . .")     


            elif "Details group: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Details group: ","")
                    if gid in [""," "]:
                        nadya.sendText(msg.to,"กลุ่ม id ไม่ถูกต้อง")
                    else:
                        try:
                            groups = nadya.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            nadya.sendText(msg.to,h)
                        except Exception as error:
                            nadya.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = nadya.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                nadya.rejectGroupInvitation(i)
                            except:
                                nadya.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        nadya.sendText(msg.to,"ปฏิเสธคำเชิญจากกลุ่มสำเร็จแล้ว " + gid.name)
                    else:
                        nadya.sendText(msg.to,"ไม่พบกลุ่ม")
            
            elif msg.text in ["Acc invite"]:
                if msg.from_ in admin:
                    gid = nadya.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = nadya.getGroup(i)
                            _list += gids.name
                            nadya.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        nadya.sendText(msg.to,"ยอมรับคำเชิญทั้งหมดจากกลุ่มแล้ว :\n" + _list)
                    else:
                        nadya.sendText(msg.to,"ไม่มีกลุ่มที่รอดำเนินการในขณะนี้")  


            elif "Gif gore" in msg.text:
            	gif = ("https://media.giphy.com/media/l2JHVsQiOZrNMGzYs/giphy.gif","https://media.giphy.com/media/OgltQ2hbilzJS/200w.gif")
                gore = random.choice(gif)
                nadya.sendGifWithURL(msg.to,gore)




        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = nadya.fetchOps(nadya.Poll.rev, 5)
    except EOFError:
        raise Exception("อาจมีการแก้ไขผิดพลาด\n" + str(nadya.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            nadya.Poll.rev = max(nadya.Poll.rev, Op.revision)
            bot(Op)

