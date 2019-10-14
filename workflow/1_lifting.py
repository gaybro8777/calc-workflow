from lexibank_chenhmongmien import Dataset as ds
from lingpy import *

wl = Wordlist.from_cldf(
        ds().dir.joinpath('cldf','cldf-metadata.json'),
        )

languages = [
        "EasternLuobuohe",
        "Chuanqiandian",
        "CentralGuizhouChuanqiandian",
        "WesternXiangxi",
        "EasternXiangxi",
        "Bana",
        "Younuo",
        "Numao"
        "EasternBahen",
        "WesternBaheng",
        "EasternQiandong",
        "WesternQiandong",
        "BiaoMin",
        "ZaoMin"] # modify

wl.output('tsv', filename='D_Chen_subset',
        prettify=False,
        subset=True,
        rows=dict(doculect='in '+str(languages))
        )

wl = Wordlist('D_Chen_subset.tsv')
print('Wordlist has {0} concepts and {1} varieties across {2} words.'.format(
    wl.height, wl.width, len(wl)))

# do I need a namespace argument there? It runs fine without the namespace argument

# merger? merge with Chen's old reconstruction?

