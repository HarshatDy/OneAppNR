 kubectl edit configmap -n kube-system kube-proxy
 kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.14.8/config/manifests/metallb-native.yaml
 kubectl get pods -n metallb-system
 

vim metallb-ippool.yml
kubectl -n metallb-system apply -f metallb-ippool.yml 


 kubectl get IPAddressPool -n metallb-system
 vim l2-advertisement.yaml
 kubectl apply -f l2-advertisement.yaml 
 
