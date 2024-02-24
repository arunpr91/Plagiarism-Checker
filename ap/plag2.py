import chk
import jac
import convert
from flask import Flask, request, render_template 


app = Flask(__name__)
@app.route('/', methods =["GET", "POST"])


def main():
    if request.method == "POST":
        valdict = request.form
        list1 = list(valdict.values())
        document1 = str(list1[1])
        document2 = str(list1[2])
        document1= convert.conv(document1)
        document2= convert.conv(document2)
        p = float(list1[3])
        option = request.form.getlist('options')
        # Convert the similarity threshold to a float

        cleaned_doc1 = chk.clean_text(document1)
        cleaned_doc2 = chk.clean_text(document2)

        similarity = jac.jaccard_similarity(cleaned_doc1, cleaned_doc2)
        similarity_percentage = round(similarity * 100, 2)

        if similarity_percentage >= p:
            result = "These documents may contain similar content."
        else:
            result = "These documents appear to be dissimilar."

        # Render the results using an HTML template
        return render_template("result.html", result=result, similarity=similarity_percentage)

    return render_template("form1.html")




if __name__=='__main__':
   app.run(debug=True,port=8080)

