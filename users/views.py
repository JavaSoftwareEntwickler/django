from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from libri import views as libriviews




def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:

            try:
                login(request, user)
                # Redirect to a success page.

                try:
                    return libriviews.libri(request)
                except Exception as e:
                    print('eccezione redirect', e)
                else:
                    pass
                finally:
                    pass
            except Exception as e:
                print("eccezione", e)
                pass
            else:
                pass
            finally:
                pass
        else:
            # Return an 'invalid login' error message.
            messages.success(request, 'Errore durante la login')
            return render(request, 'authenticate/login.html',{})
    else:
        return render(request, 'authenticate/login.html',{})
    print('fineeeeeeeeee')

def logout_user(request):
    return render(request, 'authenticate/logout.html',{})
