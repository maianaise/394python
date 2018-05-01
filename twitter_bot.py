import tweepy, time

ck = 'uPV8HPO5rnfVKA8lsaYDc3eGg'
cs = 'FD0w9EAyElQK7CqZVIx4FJE4332n5dEfxPNPMOBJ6o5IoELLmh'
ak = '986082748426342400-qsj2rCyf3DKyGEjBVbn4ud6qouLzlgx'
ase = 'Uv4pnHh8UqPE7jsnebSXtLG442T4dXZCBybqaye6NuWdF'
auth = tweepy.OAuthHandler(ck, cs)
auth.set_access_token(ak, ase)
api = tweepy.API(auth)
 


filename = "til.txt"

def twitter():
    a = open(filename,'r')
    file = a.read()
    a.close()
    api.update_status(file)

while True:
    twitter()
    time.sleep(7200)

