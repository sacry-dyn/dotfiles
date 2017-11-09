import re
import sys


def normalize(t: str) -> str:
  invalid = "invalid_title"
  if not t:
    return invalid

  s = re.sub('[^A-Za-z0-9]+', '_', t)
  s = re.sub('\_+', '_', s)

  s = s.lower().strip()
  tokens = s.split("_")
  tokens = [token for token in tokens if len(token) > 2]
  s = "_".join(tokens)

  if not s:
    return invalid

  if s[0] == "_":
    s = s[1:]

  if s[-1] == "_":
    s = s[:-1]

  return s

def test_normalize():
  s = "LSTM-based Encoder-Decoder for Multi-sensor Anomaly Detection"
  n = normalize(s)
  assert n == "lstm_based_encoder_decoder_for_multi_sensor_anomaly_detection"
  print("from: {}\nto: {}".format(s,n))

def main(s: str):
  print("{}.pdf".format(normalize(s)))

if __name__ == "__main__":
  test_normalize()
  # args = " ".join(sys.argv[1:])
  # main(args)



