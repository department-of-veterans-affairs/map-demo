require File.expand_path '../test_helper.rb', __FILE__

class TestHashService < MiniTest::Unit::TestCase

  include Rack::Test::Methods

  def app
    Sinatra::Application
  end

  def test_service_running
    get '/'
    assert last_response.ok?
    assert_equal "hash_service running on #{Socket.gethostname}\n", last_response.body
  end
end