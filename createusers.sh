#! /bin/bash
#
# createBatch.sh BATCH_FILE
# BATCH_FILE FORMAT: EMAIL ID# FIRST_NAME LAST_NAME
#

SEMESTER=XX

cat $1 | while read line; do
	user=`echo $line | awk -F@ '{print $1}'`
	pass=`echo $line | awk '{print $2}'`
	full_name=`echo $line | awk '{print $3, $4}'`
	
	ypmatch $user passwd
	return=`echo "$?"`

	if [ "$return" = "1" ];then
		useradd -m -c "$full_name" -g student -s /bin/csh -d /home/$SEMESTER/$user $user 
		echo "p$pass" | passwd --stdin $user

		for i in cdsenv cdsinit cds.lib tcshrc tcshrc_synopsys ; do
			cp /etc/skel/$i /home/$SEMESTER/$user/.$i
		done
	
		chown -R $user.student /home/$SEMESTER/$user
		chmod -R 700 /home/$SEMESTER/$user  #Readable only by owner
		echo "$line" >> NewUser
	else
		echo "$user already exists" >> Existing_accounts
	fi
done

sort Existing_accounts | uniq >> E_acct.tmp
mv E_acct.tmp Existing_accounts
make -C /var/yp
