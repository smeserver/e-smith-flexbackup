# $Id: e-smith-flexbackup.spec,v 1.2 2008/10/07 18:14:27 slords Exp $

Summary: Adds daily flexbackup backup to tape to e-smith
%define name e-smith-flexbackup
Name: %{name}
%define version 2.0.0
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-base, flexbackup, dump
Requires: buffer
Requires: mbuffer
Requires: tar
Requires: gzip
Requires: e-smith-backup >= 1.11.0-46
Requires: e-smith-lib >= 1.15.1-19
BuildRequires: e-smith-devtools >= 1.13.1-03
AutoReqProv: no

%description
This package configures flexbackup and sets up a daily cron job
to run a backup to tape.

%changelog
* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 2.0.0-1.sme
- Roll new stream to separate sme7/sme8 trees [SME: 4633]

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Thu Apr 20 2006 Charlie Brady <charlie_brady@mitel.com> 1.10.0-02
- Remove redundant "mt fsf" from DetermineBlocksize(). [SME: 1191]

* Wed Mar 15 2006 Charlie Brady <charlie_brady@mitel.com> 1.10.0-01
- Roll stable stream version. [SME: 1016]

* Mon Jan 23 2006 Charlie Brady <charlieb@e-smith.com> 1.9.0-18
- Fix spelling of blksize parameter when running flexbackup to restore.
  [SME: 375]

* Sun Jan 22 2006 Charlie Brady <charlieb@e-smith.com> 1.9.0-17
- Fix some perl warnings from last change. [SME: 375]

* Sun Jan  8 2006 Charlie Brady <charlieb@e-smith.com> 1.9.0-16
- Autodetect tape block size and use that when extracting files, rather
  that what is in flexbackup.conf [SME: 375]

* Sat Dec 25 2005 Gordon Rowell <gordonr@gormand.com.au> 1.9.0-15
- Avoid the use of mt tell - use mt status instead [SME: 320]

* Sat Dec 17 2005 Charlie Brady <charlieb@e-smith.com> 1.9.0-14
- Remove attempted autdetection of backup type, since it doesn't
  work. [SME: 340]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.9.0-13
- Bump release number only

* Sun Nov 20 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-12]
- Output nothing (not '0') when there is no prune list [SF: 1360696]

* Thu Oct 20 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-11]
- Allow a Prune property to specify a list of subtrees which are
  not included in the backup. [SF: 1332834]

* Thu Oct 20 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-10]
- Don't bother to backup /boot partition, as we never restore it
  anyway. We expect it all to be installed via CDROM or as part of
  an upgrade. [SF: 1332834]

* Tue Aug  9 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-09]
- Make buffer program to use configurable via a db property -
  default to 'buffer'.
- Add Requires: mbuffer [SF: 1252345]

* Tue Jul 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-08]
- Update to current db access APIs. [SF: 1216546]

* Thu Jun  2 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-07]
- Fix missing semi-colon on erase_rewind_only line in conf.
  [SF: 1192822,1213076]
- Adjust some default params. [SF: 1213076]

* Sat Apr 30 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-06]
- Fix quoting of erase_rewind_only value [SF: 1192822]

* Mon Mar 14 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-05]
- Fix stray } in 10EraseRwindOnly template fragment (introduced in last
  change set).

* Mon Mar 14 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-04]
- Use generic_template_expand action in place of conf-flexbackup.
  Add default db property fragments. Update e-smith-lib dependency. [MN00064130]
- Simplify flexbackup.conf template, and remove anachronisms.

* Fri Jan 28 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-03]
- Remove dangling clobber-flexbackup-cron symlink. [MN00065727]

* Tue Jan 25 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-02]
- Remove obsolete clobber-flexbackup-cron action. [MN00065727]

* Sun Jan 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-01]
- Changing version to development stream number - 1.9.0

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Changing version to stable stream number to 1.8.0

* Thu Jun 19 2003 Charlie Brady <charlieb@e-smith.com>
- [1.7.1-07]
- Enable buffering using "buffer" rather than "mbuffer". [charlieb 9053]

* Wed Jun 18 2003 Charlie Brady <charlieb@e-smith.com>
- [1.7.1-06]
- Autodetect tar/dump at restore time and DTRT. [charlieb 8965]
- Disable buffering during restore. [charlieb 9053]

* Thu Jun 12 2003 Charlie Brady <charlieb@e-smith.com>
- [1.7.1-05]
- Change default backup type from dump to tar. Allow override from config
  db. [charlieb 8965]

* Thu Jun 12 2003 Charlie Brady <charlieb@e-smith.com>
- [1.7.1-04]
- Fix quoting error in 10Blocksize fragment, and split concepts of blocking
  for archive and blocking for tape drive, as latest flexbackup has done.
  [charlieb 9014]

* Thu Jun 12 2003 Charlie Brady <charlieb@e-smith.com>
- [1.7.1-03]
- Add tape-backup-flexbackup action, which will be used by
  /sbin/e-smith/do_backup harness. Remove remnant of templated backup
  program. [charlieb 7853]
- Set $verbose to false, so we don't get list of all files as we backup.
  [charlieb 8965]

* Thu Jun 12 2003 Charlie Brady <charlieb@e-smith.com>
- [1.7.1-02]
- Port configuration to newest version of flexbackup. [charlieb 9014]
- s/Copyright/License/.

* Thu Jun 12 2003 Charlie Brady <charlieb@e-smith.com>
- [1.7.1-01]
- Roll new development stream to 1.7.1

* Thu Jun 12 2003 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-04]
- Allow blocksize to be controlled by a db parameter. [charlieb 9017]

* Fri May 16 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-03]
- Modified tape-restore-flexbackup to use esmith::Backup library [gordonr 8766]

* Wed Apr 16 2003 Tony Clayton <apc@e-smith.com>
- [1.7.0-02]
- Skip loopback filesystems during backup [tonyc 7749]

* Wed Nov  6 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-01]
- Rolling development stream version to 1.7.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-01]
- Roll to maintained version number to 1.6.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-01]
- Roll to maintained version number to 1.6.0

* Fri Aug  9 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.2-01]
- Redo last fix, something's awry with my pattern match, so we'll use a
  pair of eqs instead. [charlieb 4588]

* Fri Aug  9 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.1-01]
- Change fstab grok in flexbackup.conf template to handle ext3 file
  systems. [charlieb 4588]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-01]
- Changing version to maintained stream number to 1.5.0

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-01]
- Changing version to maintained stream number to 1.4.0
- Remove bogus "/sbin/console" reference in copyright notice in 
  tape restore script.

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.3-01]
- RPM rebuild forced by cvsroot2rpm

* Sun Mar 17 2002 Charlie Brady <charlieb@e-smith.com>
- [1.3.2-01]
- Restore /root rather than just /root/.ssh. [charlieb #2322]

* Sun Mar 17 2002 Charlie Brady <charlieb@e-smith.com>
- [1.3.1-01]
- Test build to verify CVS conversion.

* Sun Mar 17 2002 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-01]
- rollRPM: Rolled version number to 1.3.0-01. Includes patches up to 1.2.0-08.
- Add mkdir command to create event directories to %pre section, in preparation
  for CVS conversion.
- Remove obsolete %post script.

* Fri Nov 02 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-08]
- Remove all comments from /etc/flexbackup.conf

* Fri Aug 17 2001 gordonr
- [1.2.0-07]
- Autorebuild by rebuildRPM

* Fri Jul 6 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-06]
- Changed license to GPL

* Mon Feb 12 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-05]
- rolling release number for GPG signing.

* Sun Feb 11 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-04]
- Include etc/e-smith/templates-user-custom in restore fileset.

* Thu Feb  8 2001 Adrian Chung <adrianc@e-smith.com>
- Rolling release number for GPG signing.

* Thu Feb 8 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-02]
- Using correct path for /flexbackup.extract.log in email messages.

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-01]
- Rolled version number to 1.2.0-01. Includes patches upto 1.1.0-10.

* Wed Jan 24 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-10]
- Removed duplicated filesystem code from 10Compression template fragment

* Tue Jan 23 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-09]
- Forced padding of blocks when writing to tapes

* Sat Jan 13 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-08]
- revised order of files to restore - doesn't really make any
  difference, but it keeps it consistent with e-smith-backup

- [1.1.0-07]
- added missing use esmith::db to tape-restore-flexbackup

* Sat Jan 13 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-06]
- tape-restore-flexbackup now send mail to admin on success or failure

* Fri Jan 12 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-05]
- Added flexbackup specific tape-restore program (ripped out of
  e-smith-backup).
- Removes /etc/cron.d/flexbackup as part of bootstrap-console-save
- Createlinks is now a perl program.

* Fri Jan 12 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-4]
- Fix silly syntax errors in template
- Migrate old flexbackup service entry to new.

* Fri Jan 12 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-3]
- Make e-smith-flexbackup a subpackage of e-smith-backup
- Provide a template fragment for /sbin/e-smith/backup
- Use Device property of backup service.
- Mark flexbackup as a backupservice, not a service.
- Add link into bootstrap-console-save and conf-backup events

* Thu Jan 11 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-02]
- Ensured that /sbin is included in $PATH for flexbackup cron job

* Tue Jan 9 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-01]
- Rolled version number to 1.1.0-01. Includes patches upto 0.1-11

* Mon Jan 8 2001 Peter Samuel <peters@e-smith.com>
- [0.1-11]
- Cron job now rewinds the tape after the backup

* Sat Jan 6 2001 Jason Miller <jmiller@e-smith.com>
- [0.1-9]
- updated /etc/cron.d/flexbackup template and the conf-flexbackup
  actions to include new configuration database parameters
  of backupTime and reminderTime

* Sat Jan 6 2001 Charlie Brady <charlieb@e-smith.com>
- [0.1-8]
- Only run %post sript when in runlevel 7

* Wed Jan 3 2001 Peter Samuel <peters@e-smith.com>
- [0.1-7]
- Added use esmith::db to /etc/cron.d/flexbackup template

* Wed Dec 27 2000 Peter Samuel <peters@e-smith.com>
- [0.1-6]
- Crontab entry now uses mt to check for presence of tape before
  running flexbackup.
- A reminder is mailed to root if there is no tape in the drive at 2pm.

* Thu Dec 14 2000 Charlie Brady <charlieb@e-smith.com>
- Move crontab entry to /etc/cron.d
- Make device and erase_backup_only configurable.
- make this a service in the configuration db, by default service is
  disabled.

* Tue Dec 12 2000 Charlie Brady <charlieb@e-smith.com>
- Make flexbackup.conf a directory template
- Tweak a few settings - see patch for details.

* Mon May 22 2000 Charlie Brady <charlieb@e-smith.net>
- Generate file system list from /etc/fstab
- Fix missing %conf declaration in action script

* Mon May 22 2000 Charlie Brady <charlieb@e-smith.net>
- Fix spec file to include all relevant files
- Fix post script : cron -> crond

* Sun May 14 2000 Charlie Brady <charlieb@e-smith.net>
- Initial build

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%post
rm -f /etc/cron.d/flexbackup

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
