pipeline(
        "AwsJenkins":{
            node ('ops-school-dynamic-slave'){                

                stage('Checkout'){
                    checkout scm
                }

                stage('Directory'){
                    dir('weather'){
                        git url: 'https://github.com/GuyElad/opsschool3-coding.git'
                }

                stage('RunScript'){
                    #!/bin/bash
                    sh 'cd /home/ubuntu/workspace/weather/home-assignments/session1'				
                    sh 'sudo pip3 install click weather-api'
		    sh 'chmod +x ./cly.py'
		    sh 'python3 ./cly.py --city dublin --forecast TODAY+3 -c'
                }

            }

        }
)
