from django.shortcuts import redirect, render


def handler404(request, *args, **argv):
    if request.path.endswith(".html"):
        return redirect(request.path.replace(".html", ""))

    if request.path.endswith(".htm"):
        return redirect(request.path.replace(".htm", ""))

    response = render(request, "pages/404.html")
    response.status_code = 404
    return response
