ENV['RACK_ENV'] = 'test'
require 'minitest/autorun'
require 'rack/test'

require File.expand_path '../../hash_service.rb', __FILE__