var chai = require('chai');
var chaiHttp = require('chai-http');
var sinon = require('sinon');
var server = require('../web_frontend.js');
var fakeredis = require('fakeredis');
var redis = require('redis');

var should = chai.should();

chai.use(chaiHttp);

describe('Frontend', function() {
    before(function(){
        sinon.stub(redis, 'createClient').callsFake(fakeredis.createClient);
        client = redis.createClient();
    });
    after(function(){
        redis.createClient.restore();
    });
    it('should return 200 on / GET', function(done) {
        chai.request(server)
            .get('/')
            .end(function(err, res){
                res.should.have.status(200);
                res.body.should.be.a('object');
                done();
        });
    });
    it('should return 200 on /index.html GET', function(done) {
        chai.request(server)
            .get('/index.html')
            .end(function(err, res){
                res.should.have.status(200);
                res.body.should.be.a('object');
                done();
        });
    });
});