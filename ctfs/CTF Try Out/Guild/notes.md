I'm still a noob, so I'm going to read this. 

<https://medium.com/@alephus/hackthebox-tryout-ctf-guild-writeup-31cda31ba10e>

SSTI!

{{ User.query.filter(User.username=="admin").first().email }}

753735754e377464@master.guild


...

It's really strange, I can't get `/verify` to work. I can't continue the CTF without it. I'm going to give up and switch to a different lab.