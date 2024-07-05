pipeline{
    agent { label "localhost" }
    tools{
        maven 'maven'
    }
    stages{
        stage("clone")
        {
            steps{
                git 'https://github.com/vPt-King/javatomcat-k8s-jenkins-ansible.git'
            }
        }
        stage("test")
        {
            steps{
                sh "mvn clean test"
            }
        }
        stage("build")
        {
            steps{
                sh "mvn clean install"
            }
        }
    }
}