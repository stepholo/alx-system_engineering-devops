#!/usr/bin/env ruby
puts ARGV[0].scan(/^[^\D]\d{10}/).join
