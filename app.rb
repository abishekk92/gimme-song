require "sinatra"
require 'koala'
require 'json'
require 'youtube_search'
enable :sessions
set :raise_errors, false
set :show_exceptions, false 
configure :development do
ENV["FACEBOOK_APP_ID"]="391867550875701"
ENV["FACEBOOK_SECRET"]="ba24216257756039c68ad2f050c63f0d"
end 

FACEBOOK_SCOPE = 'user_likes,user_photos,user_photo_video_tags,user_interests'

unless ENV["FACEBOOK_APP_ID"] && ENV["FACEBOOK_SECRET"]
  abort("missing env vars: please set FACEBOOK_APP_ID and FACEBOOK_SECRET with your app credentials")
end


interest_graph=Array.new

before do
  # HTTPS redirect
  if settings.environment == :production && request.scheme != 'https'
    redirect "https://#{request.env['HTTP_HOST']}"
  end
end

helpers do
  def host
    request.env['HTTP_HOST']
  end

  def scheme
    request.scheme
  end

  def url_no_scheme(path = '')
    "//#{host}#{path}"
  end

  def url(path = '')
    "#{scheme}://#{host}#{path}"
  end

  def authenticator
   @authenticator ||= Koala::Facebook::OAuth.new(ENV["FACEBOOK_APP_ID"], ENV["FACEBOOK_SECRET"], url("/auth/facebook/callback"))
  end

end

# the facebook session expired! reset ours and restart the process
error(Koala::Facebook::APIError) do
  session[:access_token] = nil
  redirect "/auth/facebook"
end

get "/" do
  # Get base API Connection
  @graph  = Koala::Facebook::API.new(session[:access_token])

  # Get public details of current application
  @app  =  @graph.get_object(ENV["FACEBOOK_APP_ID"])
  #user_interest_graph=Array.new
  if session[:access_token]
    @user    = @graph.get_object("me")
    @friends = @graph.get_connections('me', 'friends')
    @photos  = @graph.get_connections('me', 'photos')
    @likes   = @graph.get_connections('me', 'likes').first(4)
    @music   = @graph.get_connections('me', 'music')
    @friends_using_app = @graph.fql_query("SELECT uid, name, is_app_user, pic_square FROM user WHERE uid in (SELECT uid2 FROM friend WHERE uid1 = me()) AND is_app_user = 1")
     user_interest_graph = @music.each { |music| music['name'] }
    
   File.open('user_graph/'+"#{@user['name']}.json","w") do |f|
   f.write(user_interest_graph.to_json)
  end
 end
  erb :index
end

# used by Canvas apps - redirect the POST to be a regular GET
post "/" do
  redirect "/"
end

# used to close the browser window opened to post to wall/send to friends
get "/close" do
  "<body onload='window.close();'/>"
end

get "/sign_out" do
  session[:access_token] = nil
  redirect '/'
end

get "/auth/facebook" do
  session[:access_token] = nil
  redirect authenticator.url_for_oauth_code(:permissions => FACEBOOK_SCOPE)
end

get '/auth/facebook/callback' do
	session[:access_token] = authenticator.get_access_token(params[:code])
	redirect '/'
end

get '/upload' do

erb :upload 

end 
get '/music/discover/:user' do 
  current_user=params[:user]
  interest_graph_json=File.read("user_graph/#{current_user}.json")
  interest_graph=JSON.parse(interest_graph_json)
  if interest_graph.empty?
     @yotube=YoutubeSearch.search('','category'=>'Music','orderby'=>'viewCount',:page=>1,:per_page=>10)

  else 
  discovery_array=interest_graph.map{ |interest|  interest['name'] }
  @youtube = discovery_array.map do |search_term|
        YoutubeSearch.search(search_term).first['video_id'] 
   end 
  end 
  erb :video  

end 


post '/upload' do
File.open('music/' + 'song_buffer.mp3' ,"w") do |f|
f.write(params['myfile'][:tempfile].read)
end

redirect '/music/discover'

end



