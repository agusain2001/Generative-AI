from flask import Flask, render_template,jsonify, request
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTempate
from langchain.chains import LLMChain, SimpleSeqentialChain,
SequentialChain





app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate', methods=[ 'POST', 'GET'])
def generate():
  if request.method == 'POST':
    prompt = PromptTempate.from_template("Generate a blog on title {title}?")
    llm = OpenAI(temperature =0.3)
    chain1 = LLMChain(llm=llm,prompt=prompt)
    prompt = request.json.get('prompt')
    output = chain.run(prompt)
    return output


app.run(host='0.0.0.0', port=81)
