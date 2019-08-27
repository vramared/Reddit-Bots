import praw
import config

def bot_login():
	r = praw.Reddit(username = config.username, 
			password = config.password, 
			client_id = config.client_id, 
			client_secret = config.client_secret,
			user_agent = "test")
	return r

def run_bot():
	user = r.redditor('bearownage')
	i = 0
	for comment in user.comments.new():
			
		print(comment.body)
		comment.reply("Hi! My records are showing that you are a past/present/future Yonsei University Student! Yonsei University (Hangul: 연세대학교; Hanja: 延世大學校; [jʌn.seː]) is a private research university in Seoul, South Korea. It is one of Korea's three SKY universities, considered the most prestigious in the country. Yonsei was established in 1885 and is one of the oldest universities in South Korea. The student body consists of 26,731 undergraduate students, 11,994 graduate students, 4,518 faculty members, 6,788 staff, and 257,931 alumni. Yonsei operates its main campus in Seoul and offers graduate, postgraduate and doctoral programs in Korean and English. The university was established in January 1957 through the union of Yonhi College (연희전문학교; 延禧專門學校) and Severance Union Medical College (세브란스 의과대학; 세브란스 醫科大學). This was a result of a lasting bilateral cooperation between the colleges that began in the 1920s. The institutions were new to Korea at the time of their inception. Yonhi College was one of the first modern colleges, founded as Chosun Christian College (조선기독교대학; 朝鮮基督教大學) in March 1915. Severance has its roots in the first modern medical center in Korea, Gwanghyewon (광혜원 廣惠院, House of Extended Grace), founded in April, 1885. As a tribute, the name 'Yonsei' was derived from the first syllables of the names of its two parent institutions, 'Yon; 연; 延' from Yonhi College and 'Sei; 세; 世' from Severance Union Medical College.")


r = bot_login()
run_bot()
