echo "============================="
echo "====== StormBOT ========"
echo "=== Created By Storm ========"
echo "==== Twitch ===="
echo "=== Centos Support only Maybe====="

if [[ "$1" == "start" ]]; then
   echo "Starting Server"
   nohup python3 stormbot.py &

elif [[ "$1" == "stop" ]]; then
   echo "Stopping Server"
   ps aux | grep -ie stormbot.py | awk '{print $2}' | xargs kill -9

elif [[ "$1" == "install" ]]; then
   python -m pip install -r install_stuff/requirements.txt

else
   echo "No Argument Found Please follow the instructions below"
   echo "start.sh <start|stop|install>"

fi