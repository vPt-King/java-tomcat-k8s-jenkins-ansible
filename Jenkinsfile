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
        stage("build and push image")
        {
            // steps{
            //     ansiblePlaybook credentialsId: 'thanhnga', installation: 'Ansible', inventory: '/var/lib/jenkins/workspace/java-tomcat/inventory.ini', playbook: '/var/lib/jenkins/workspace/java-tomcat/ansible.yml', vaultTmpPath: ''
            // }
            steps{
                // This step should not normally be used in your script. Consult the inline help for details.
                withDockerRegistry(credentialsId: '573f4d52-0eea-43a5-95bc-fa8dda139b5b', url: 'https://index.docker.io/v1/') {
                    sh "docker login -u thanhvu638 -p Conbo2chan@"
                    sh "docker build -f Dockerfile -t thanhvu638/javaweb:${BUILD_ID} ."
                    sh "docker push thanhvu638/javaweb:${BUILD_ID}"
                }
            }
        }
        stage("ansible")
        {
            steps{
                ansiblePlaybook credentialsId: 'thanhnga', installation: 'Ansible', inventory: '/var/lib/jenkins/workspace/java-tomcat/inventory.ini', playbook: '/var/lib/jenkins/workspace/java-tomcat/ansible.yml', vaultTmpPath: '', extras: "version=${BUILD_ID}"
            }
        }
    }
}