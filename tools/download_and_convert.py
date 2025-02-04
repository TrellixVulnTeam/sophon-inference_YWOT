""" Download test data, or download and convert models
Usage: python download_and_convert.py googlenet
"""
from __future__ import print_function
import os
import argparse
from sophon.utils.download_and_convert import download_data
from sophon.utils.download_and_convert import download_model
from sophon.utils.download_and_convert import convert2bmodel
from sophon.utils.download_and_convert import download_and_convert


def main():
  """Program entry point.
  """
  base_url = 'https://sophon-file.sophon.cn/sophon-prod-s3/model/19/06/27/'
  # base_url = 'http://10.30.34.184:8080/sophon_model/'
  save_dir = FLAGS.save_path
  model_dir = os.path.join(save_dir, 'models')
  model_list = [
      'fasterrcnn_resnet50_tf',
      # 'deeplabv3_mobilenetv2_tf',
      # 'fasterrcnn_vgg',
      'mtcnn',
      'mtcnncxx',
      'ssh',
      'yolov3',
      # 'yolov3_mx',
      'resnet50_pt',
      'resnext50_mx',
      'googlenet',
      'resnet50',
      'vgg16',
      'mobilenetv1',
      'mobilenetv1_tf',
      'mobilenetssd',
      'mobilenetyolov3',
  ]
  if FLAGS.arg == 'all':
    ret = download_data(base_url, save_dir)
    if not ret:
      print("Failed to download test_data")
      exit(-1)
    print('')
    if not os.path.exists(model_dir):
      os.makedirs(model_dir)
    for model_name in model_list:
      download_and_convert(base_url, model_dir, model_name)
      print('')
  elif FLAGS.arg == 'model_list':
    print("default model list:")
    for name in model_list:
      print("- {}".format(name))
  elif FLAGS.arg == 'test_data':
    ret = download_data(base_url, save_dir)
    if not ret:
      print("Failed to download test_data")
      exit(-1)
  elif FLAGS.arg in model_list:
    if not os.path.exists(model_dir):
      os.makedirs(model_dir)
    download_and_convert(base_url, model_dir, FLAGS.arg)
  else:
    raise ValueError('Invalid argument', FLAGS.arg)

if __name__ == '__main__':
  sophon_model_dir = os.getenv('SOPHON_MODEL_DIR',os.getenv('HOME'))
  default_save_dir = os.path.join(sophon_model_dir, '.sophon/')

  PARSER = argparse.ArgumentParser(\
      description='Download test data, or download and convert models.')
  PARSER.add_argument(
      "arg",
      type=str,
      help="Options: model_name, 'model_list', 'test_data', 'all'")
  PARSER.add_argument(
     "--save_path",
     type=str,
     default=default_save_dir,
     help="Save sophon test model and test data."
  )
  FLAGS, UNPARSED = PARSER.parse_known_args()
  main()

