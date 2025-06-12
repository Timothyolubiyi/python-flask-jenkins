pipeline{
    agent any
    stages{
         stage("GitHub checkout....") {
            steps {
                script {
 
                    git branch: 'main', url: 'https://github.com/Timothyolubiyi/python-flask-jenkins.git' 
                }
            }
        }
        stage("Build docker connecting....."){
            steps{
                sh 'printenv'
                sh 'git version'
                sh 'docker build . -t smartgigsctf/f-app1.0'
            }
        }
         stage("push image to DockerHub"){
            steps{

               script {
                
                  
                 withCredentials([string(credentialsId: 'DockerID', variable: 'DockerID')]) {
                    sh 'docker login -u smartgigsctf -p ${DockerID}'
            }
              sh 'docker push smartgigsctf/f-app1.0:latest'
            }
        }
    }
    }
}
