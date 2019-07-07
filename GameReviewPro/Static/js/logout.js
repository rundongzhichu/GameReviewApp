function logout() {
    if (confirm('系统提示，您确定要退出本次登录吗?')) {
        location.href = "home(HTML).html";
    }
}