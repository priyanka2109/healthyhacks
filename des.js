console.log("Getting tweets for you");
var Twit = require("twit");
var config = require("./config");
var T = new Twit(config);
var params = {
  q: "design",
  count: 10,
};
T.get("search/tweets", params, gotData);
function gotData(err, data, response) {
  console.log(data);
}
