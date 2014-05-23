#!/usr/bin/env python
# -*- coding: utf-8 -*-
i = open("index.html", "w")
i.write( "<h1>Albanian Name Finder</h1>")
i.write( "<img src='Flag_of_Albania.png'/>")
i.write( "<p>Click on a state. You will get a list of names, each one will open a search on the whitepages. Exact matches will display first.</p>")
for s in ('Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming') :
    sfile = "%s.html" %s
    o = open(sfile, "w")
    i.write( '<ul><a href="' + sfile + '">'+ s + "</a></ul>\n")
    o.write( "<h1>" + s + "</h1>")
    o.write( "<ul>")
    for x in ['Agani','Ahmetaj','Ahmeti','Ajeti','Albrup','Alia','Alibali','Alii','Alikaj','Aliti','Aliu','Amiti','Arbnori','Bajraktari','Bajrami','Bajramovic','Bardha','Bardhi','Bardici','Bardulla','Bazhunaishvili','Bejko','Bejta','Berisha','Berishaj','Bislimi','Bizi','Blaku','Boja','Boshnjaku','Broci','Brozi','Budo','Bufi','Bunjaku','Bushaj','Bushati','Buzoku','Bytygi','Cacaj','Cana','Cano','Carcani','Ceka','Cela','Celaj','Chani','Chocholi','Ciftja','Cobaj','Corbajram','Culaj','Cumani','Daci','Dedej','Dejti','Demachi','Demaci','Demai','Demisovski','Dhamo','Dibra','Dosti','Dreshaj','Duka','Dzaferi','Elezi','Emini','Fakaj','Fazliu','Frasheri','Gacaferi','Galica','Galimuna','Gashi','Gecaj','Gjika','Gjikokaj','Gjinali','Gjokaj','Gozhita','Grazdani','Hajdaraga','Hajdari','Hajdini','Halii','Halil','Halili','Haliti','Hamiti','Hamza','Harxhi','Hasangjekaj','Hasani','Hassan','Haxhi','Haxhiu','Hisari','Hoxha','Hyseni','Hysi','Idrizi','Isai','Ismaili','Istogu','Isufaj','Januzaj','Jasari','Julia','Kadare','Kalaj','Kaleci','Kapllani','Kartallozi','Kastrati','Kiuprili','Kochiu','Kola','Kolcei','Kolonja','Kona','Kongoli','Korkizoglou','Kotta','Koçi','Kraja','Krasnicki','Krasniki','Krasniqi','Krizi','Kula','Kupi','Kursumulu','Kutishi','Lamaj','Latifi','Lazami','Logoreci','Lokaj','Lucca','Luga','Lumaj','Lumani','Lushi','Luzaj','Mala','Mali','Maniani','Manjani','Marishta','Marku','Maxharraj','Maxhuni','Meco','Meidani','Meksi','Meshkalla','Metarapi','Mishaxhi','Morina','Mripa','Mujushi','Murati','Murzaku','Muslimi','Nallbani','Nano','Naçi','Nesimi','Nexhipi','Nnano','Noli','Nooja','Nuhiji','Oseku','Paloka','Peco','Pernaska','Petrela','Pipa','Pllana','Pllumi','Pocoli','Poda','Pojani','Prela','Prenkpalaj','Prifti','Prishtina','Pula','Qosja','Raco','Rama','Ramadani','Reufi','Rexhepi','Ristani','Rrustemi','Rugova','Sadiku','Sadiraj','Salihu','Saliu','Sapunxiu','Sava','Sejko','Selimi','Selmani','Seseri','Shala','Shehu','Shima','Shkelyim','Shulku','Shundi','Siliqi','Simaku','Smajlaj','Sopa','Strakosha','Sulejmani','Surroi','Syla','Sylaj','Tafaj','Tahiri','Tare','Tatari','Thaci','Thaqi','Thika','Tolaj','Tolka','Tolr','Topalli','Toptani','Troshani','Tzeka','Tzelili','Useni','Varoshi','Vata','Velo','Vercuni','Veseli','Vllasi','Vulaj','Xhaferi','Xhanari','Xhaxhka','Xhumba','Ymeri','Zagreda','Zhugli','Zhulati','Zhuzhumi','Ziberi','Zogjani','Zogu']:
        url = 'https://www.whitepages.com/name/' + x + '/' + s.replace(" ","-")
        o.write( '<li><a href=' + url + '>' + x + "</a></li>\n")
    o.write( "</ul>")
    o.close()
