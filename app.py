import os
import json
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from bs4 import BeautifulSoup
    import requests