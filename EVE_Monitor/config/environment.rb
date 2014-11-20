# Load the Rails application.
require File.expand_path('../application', __FILE__)
require 'reve'

# Initialize the Rails application.
EVEMonitor::Application.initialize!


#need to setup devise for users and admin authentication
#need to be able to setup api key injecting to be able to generate relevant unser info
#from the servers for each independent user
#devise_for :users
