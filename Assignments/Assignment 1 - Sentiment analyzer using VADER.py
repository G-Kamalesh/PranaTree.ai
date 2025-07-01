from typing import List
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class sentiment:

  def analyzer(self, reviews:List[str]):
    answer = []
    for  i in reviews:
      v = []
      score = analyzer.polarity_scores(i)
      v.append(i)
      v.append(score['compound'])
      if score['compound'] >= 0.05 :
        v.append('Positive')
      elif score['compound'] <= - 0.05 :
        v.append('Negative')
      else:
        v.append('Neutral')
      answer.append(v)
    df = pd.DataFrame(answer,columns=['Reviews','Compound Scores','Final sentiment'])
    return df


if __name__ == "__main__":
    reviews = ["The setup was a breeze, and it looks really sleek. However, the battery life is surprisingly short, which is a major letdown for daily use.",
            "I love the sound quality for music, it's truly impressive. But the microphone for calls is pretty much unusable, which defeats half its purpose.",
            "It's incredibly comfortable and lightweight, perfect for long wear. My only complaint is the software, which is buggy and crashes frequently.",
            "The price point is excellent for what you get, and the build quality feels solid. Yet, the user interface is clunky and not at all intuitive.",
            "Initially, I was thrilled with its performance – super fast and responsive. After a few weeks though, it started lagging significantly.",
            "The design is innovative and really stands out. Functionally, it's just okay; some features feel half-baked.",
            "Great for casual use, and the display is vibrant. Don't expect it to handle anything strenuous; it struggles with demanding applications.",
            "I appreciate the eco-friendly packaging and the company's commitment to sustainability. The product itself, while functional, feels a bit flimsy.",
            "The camera takes decent photos in good lighting conditions. In low light, it's practically useless, producing grainy and blurry images.",
            "Fantastic customer support, they were very helpful with my initial query. The product itself has some minor glitches that are annoying but not deal-breakers.",
            "It's compact and easy to carry around, which I love. Unfortunately, the storage capacity is far too small for my needs.",
            "The connectivity options are abundant and work flawlessly. The biggest downside is the proprietary charging cable, which is a hassle.",
            "For the price, you can't beat the features it offers. The instruction manual, however, is incredibly vague and hard to follow.",
            "The overall concept is brilliant and solves a real problem. The execution, though, leaves something to be desired; it feels unfinished.",
            "It arrived quickly and was well-packaged. The color is exactly what I wanted, but the material feels cheaper than I expected."]

    Sentiment = sentiment()
    output = Sentiment.analyzer(reviews)
    print(output)