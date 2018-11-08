import os
import secrets
from PIL import Image
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.utils import redirect
from flaskblog import app, bcrypt, db, mail
from flaskblog.forms import LoginForm, PostForm, RegistrationForm, \
    UpdateAccountForm, RequestResetForm, ResetPasswordForm
from flaskblog.models import Post, User
from flask_mail import Message









