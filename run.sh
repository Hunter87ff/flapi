lgr="\033[1;32m"
rd="\033[1;31m"

echo -e " ${lgr}
███████╗██╗      █████╗ ██████╗ ██╗
██╔════╝██║     ██╔══██╗██╔══██╗██║
█████╗  ██║     ███████║██████╔╝██║
██╔══╝  ██║     ██╔══██║██╔═══╝ ██║
██║     ███████╗██║  ██║██║     ██║
╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
${rd} --- github.com/hunter87ff ---                               
"

cd ./app
fastapi dev main.py