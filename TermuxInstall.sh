# @G4rip - < https://t.me/G4rip >
# Copyright (C) 2022
# Tüm hakları saklıdır.
#
# Bu dosya, < https://github.com/aylak-github/PyFileLock > parçasıdır.
# Lütfen GNU Affero Genel Kamu Lisansını okuyun;
# < https://www.github.com/aylak-github/PyFileLock/blob/master/LICENSE/ >
# ================================================================

DOGE="🔐 PyFileLock kütüphanesi kuruluyor..."
INFOX="📣 Telegram: @G4rip"
INFOX+="\n "
INFOX+="\n💬 Destek Grubu: @RepoHaneX"
INFOX+="\n "
INFOX+="\n💫 İŞLEM DEVAM EDERKEN UYGULAMADAN AYRILMAYIN!"
PACKAGEX="\n⏳ PAKETLERİ GÜNCELLİYORUM..."
PYTHOX="\n⌛ PYTHON KURUYORUM..."
REQUIREX="\n⌛ GEREKSİNİMLERİ KURUYORUM..."
SPACEX="\n "
clear
echo -e $DOGE
echo -e $SPACEX
echo -e $SPACEX
echo -e $PACKAGEX
echo -e $SPACEX
pkg update -y
clear
echo -e $DOGE
echo -e $SPACEX
echo -e $INFOX
echo -e $SPACEX
echo -e $PYTHOX
echo -e $SPACEX
pkg install python -y
pip install --upgrade pip
clear
echo -e $DOGE
echo -e $SPACEX
echo -e $INFOX
echo -e $SPACEX
echo -e $REQUIREX
echo -e $SPACEX
pip install wheel
pip install -U PyFileLock
python3 -m PyFileLock
