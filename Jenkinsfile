pipeline{
    agent any
    tools{
        maven 'maven'
    }
    stages{
        stage("clone")
        {
            steps{
                git 'https://github.com/vPt-King/java-tomcat-k8s-jenkins-ansible.git'
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
        stage("build image")
        {
            steps{
                withDockerRegistry(url: 'https://index.docker.io/v1/') {
                    sh "docker build -f Dockerfile -t thanhvu638/javaweb:${BUILD_ID}"
                }
            }
        }
        stage("connect ansible")
        {
            steps{
                ansiblePlaybook credentialsId: 'thanhnga', installation: 'Ansible', inventory: '/var/lib/jenkins/workspace/java-tomcat/inventory.ini', playbook: '/var/lib/jenkins/workspace/java-tomcat/ansible.yml', vaultTmpPath: ''
            }
        }
    }
}