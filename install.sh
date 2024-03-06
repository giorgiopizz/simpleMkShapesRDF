#!/bin/bash

# sourceCommand="source /root/.bashrc && mamba activate cern"
# sourceCommand="source /cvmfs/sft.cern.ch/lcg/views/LCG_103/x86_64-centos7-gcc11-opt/setup.sh"
# Not optimal because SCRAM is not setup with cmsenv... but better than nothing

fullos=$(uname -r)
split=(${fullos//./ })
os=${split[5]}

if [[ ${os:0:3} == el7 ]]; then 
	echo "Assuming el7 OS"
	sourceCommand="source /cvmfs/sft.cern.ch/lcg/views/LCG_103/x86_64-centos7-gcc11-opt/setup.sh"
elif [[ ${os:0:3} == el8 ]]; then 
	echo "Assuming el8 OS"
	sourceCommand="source /cvmfs/sft.cern.ch/lcg/views/LCG_104/x86_64-centos8-gcc11-opt/setup.sh"
elif [[ ${os:0:3} == el9 ]]; then 
	echo "Assuming el9 OS"
	sourceCommand="source /cvmfs/sft.cern.ch/lcg/views/LCG_105/x86_64-el9-gcc11-opt/setup.sh"
else
	echo "OS not recognized"
	exit
fi

eval "$sourceCommand"
python -m venv --system-site-packages myenv
source myenv/bin/activate

python -m pip install -e .[docs,dev]

python -m pip install --no-binary=correctionlib correctionlib


cd utils
mkdir -p bin

cd src && c++ hadd.cxx -o hadd2 $(root-config --cflags --libs) && cd .. && mv src/hadd2 bin/hadd2

if [ $? -ne 0 ]; then
      echo "Failed compiling hadd"
      exit 1
fi
cd ..

cat << EOF > start.sh
#!/bin/bash
$sourceCommand
source `pwd`/myenv/bin/activate
export STARTPATH=`pwd`/start.sh
export PYTHONPATH=`pwd`/myenv/lib64/python3.9/site-packages:\$PYTHONPATH
export PATH=`pwd`/utils/bin:\$PATH
EOF

chmod +x start.sh

wget https://gpizzati.web.cern.ch/mkShapesRDF/jsonpog-integration.tar.gz
tar -xzvf jsonpog-integration.tar.gz
rm -r jsonpog-integration.tar.gz
mv jsonpog-integration mkShapesRDF/processor/data/
