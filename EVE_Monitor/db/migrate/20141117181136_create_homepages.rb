class CreateHomepages < ActiveRecord::Migration
  def change
    create_table :homepages do |t|

      t.timestamps
    end
  end
end
