package kubernetes.admission
deny[msg] {
  input.spec.containers[_].image == "latest"
  msg = "latest tag not allowed"
}
