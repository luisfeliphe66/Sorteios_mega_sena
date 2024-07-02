```bash
# Instalação do Docker no Ubuntu

sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
apt-cache policy docker-ce
sudo apt install docker-ce
sudo systemctl status docker
sudo usermod -aG docker ${USER}
docker build -t my_airflow_image .
docker-compose up -d

# Instalação do Docker Compose no Ubuntu

sudo apt update
sudo apt install docker-compose
docker-compose --version

# Executando os serviços com Docker Compose

cd /caminho/para/seu/diretorio
docker-compose up -d

