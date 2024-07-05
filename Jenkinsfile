pipeline{
    agent { label "localhost" }
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
        stage("ansible")
        {
            steps{
                ansiblePlaybook installation: 'Ansible', inventory: '/var/jenkins_home/workspace/java_tomcat/inventory.ini', playbook: '/var/jenkins_home/workspace/java_tomcat/ansible.yaml', vaultTmpPath: ''
            }
        }
    }
}